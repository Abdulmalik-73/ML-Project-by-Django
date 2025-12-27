#!/usr/bin/env python
"""
Streamlit version of Haramaya House Price Prediction
Usage: streamlit run streamlit_app.py
"""
import streamlit as st
import pickle
import numpy as np
import os
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Haramaya House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    """Load the trained model"""
    model_path = os.path.join('predictor', 'model.pkl')
    try:
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


# Load dataset (if available)
@st.cache_data
def load_dataset():
    """Try multiple likely locations for the CSV and return a DataFrame or None."""
    base_dir = os.path.dirname(__file__)
    candidates = [
        os.path.join(base_dir, 'haramaya_house_data.csv'),
        os.path.join(base_dir, '..', 'haramaya_house_dataset', 'haramaya_house_data.csv'),
        os.path.join(base_dir, '..', 'haramaya_house_prediction', 'haramaya_house_data.csv'),
        os.path.join(os.getcwd(), 'haramaya_house_dataset', 'haramaya_house_data.csv'),
        os.path.join(os.getcwd(), 'haramaya_house_prediction', 'haramaya_house_data.csv'),
        os.path.join(os.getcwd(), 'haramaya_house_data.csv'),
    ]

    for p in candidates:
        path = os.path.abspath(os.path.normpath(p))
        if os.path.exists(path):
            try:
                return pd.read_csv(path)
            except Exception:
                return None
    return None

# Main app
def main():
    st.title("🏠 Haramaya House Price Prediction")
    st.markdown("---")
    
    # Load model
    model_data = load_model()
    # Load dataset (optional)
    dataset = load_dataset()
    
    if not model_data:
        st.error("❌ Model not found! Please train the model first by running: `python train_model.py`")
        return
    
    # Sidebar - Model Info
    with st.sidebar:
        st.header("📊 Model Information")
        st.metric("R² Score", f"{model_data['r2_score']:.4f}")
        st.metric("MAE", f"{model_data['mae']:,.0f} ETB")
        st.metric("RMSE", f"{model_data['rmse']:,.0f} ETB")
        st.markdown("---")
        st.info("This model predicts house prices in Haramaya Town, Ethiopia")
        st.markdown("---")
        if dataset is not None:
            if st.checkbox("📁 Show dataset (sample)"):
                st.dataframe(dataset.head(200))

            csv = dataset.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download dataset CSV", data=csv, file_name='haramaya_house_data.csv', mime='text/csv')
        else:
            st.write("Dataset not found in repository. Place `haramaya_house_data.csv` under `haramaya_house_dataset/` or next to this script.")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏡 House Features")
        bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
        bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
        house_size = st.number_input("House Size (sqm)", min_value=50, max_value=500, value=120)
        land_size = st.number_input("Land Size (sqm)", min_value=100, max_value=2000, value=300)
    
    with col2:
        st.subheader("📍 Location & Condition")
        location = st.selectbox(
            "Location",
            ["Tinike", "Harar gate area", "University area", "Gende Kore", "Quncho Ber", "Kore Hiwot"]
        )
        condition = st.selectbox(
            "House Condition",
            ["New", "Good", "Needs Renovation"]
        )
        year_built = st.number_input("Year Built", min_value=1990, max_value=2025, value=2020)
    
    st.markdown("---")
    
    # Predict button
    if st.button("🔮 Predict Price", type="primary", use_container_width=True):
        # Encode categorical variables
        le_location = model_data['le_location']
        le_condition = model_data['le_condition']
        
        location_encoded = le_location.transform([location])[0]
        condition_encoded = le_condition.transform([condition])[0]
        
        # Prepare features
        features = np.array([[
            bedrooms,
            bathrooms,
            house_size,
            land_size,
            location_encoded,
            condition_encoded,
            year_built
        ]])
        
        # Make prediction
        model = model_data['model']
        predicted_price = model.predict(features)[0]
        
        # Calculate confidence range
        lower_range = predicted_price * 0.9
        upper_range = predicted_price * 1.1
        
        # Display results
        st.success("✅ Prediction Complete!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("💰 Predicted Price", f"{predicted_price:,.0f} ETB")
        
        with col2:
            st.metric("📉 Lower Range", f"{lower_range:,.0f} ETB")
        
        with col3:
            st.metric("📈 Upper Range", f"{upper_range:,.0f} ETB")
        
        st.markdown("---")
        
        # Display input summary
        with st.expander("📋 Input Summary"):
            st.write(f"**Bedrooms:** {bedrooms}")
            st.write(f"**Bathrooms:** {bathrooms}")
            st.write(f"**House Size:** {house_size} sqm")
            st.write(f"**Land Size:** {land_size} sqm")
            st.write(f"**Location:** {location}")
            st.write(f"**Condition:** {condition}")
            st.write(f"**Year Built:** {year_built}")

if __name__ == '__main__':
    main()
