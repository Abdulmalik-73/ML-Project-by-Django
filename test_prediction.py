#!/usr/bin/env python
"""Test prediction functionality"""
import pickle
import pandas as pd
import numpy as np
import os

# Load model
model_path = os.path.join('predictor', 'model.pkl')
print(f"Loading model from: {model_path}")

with open(model_path, 'rb') as f:
    model_data = pickle.load(f)

print("Model loaded successfully!")
print(f"R² Score: {model_data['r2_score']:.4f}")
print(f"Feature names: {model_data.get('feature_names', 'Not found')}")

# Test prediction
location = 'Tinika'
condition = 'Good'

le_location = model_data['le_location']
le_condition = model_data['le_condition']

print(f"\nLocation classes: {le_location.classes_}")
print(f"Condition classes: {le_condition.classes_}")

try:
    location_encoded = le_location.transform([location])[0]
    condition_encoded = le_condition.transform([condition])[0]
    print(f"\nLocation '{location}' encoded to: {location_encoded}")
    print(f"Condition '{condition}' encoded to: {condition_encoded}")
    
    # Prepare features
    feature_names = model_data.get('feature_names', ['bedrooms', 'bathrooms', 'house_size', 'land_size', 'location', 'condition', 'year_built'])
    features = pd.DataFrame([[
        3,  # bedrooms
        2,  # bathrooms
        120,  # house_size
        500,  # land_size
        location_encoded,
        condition_encoded,
        2015  # year_built
    ]], columns=feature_names)
    
    print(f"\nFeatures DataFrame:")
    print(features)
    
    # Predict
    model = model_data['model']
    predicted_price = model.predict(features)[0]
    
    print(f"\n✅ Prediction successful!")
    print(f"Predicted price: {predicted_price:,.0f} ETB")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
