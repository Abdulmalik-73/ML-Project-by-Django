import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle
import os

# Load dataset
df = pd.read_csv('haramaya_house_data.csv')

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Prepare features and target
X = df.drop('price', axis=1)
y = df['price']

# Encode categorical variables
le_location = LabelEncoder()
le_condition = LabelEncoder()

X['location'] = le_location.fit_transform(X['location'])
X['condition'] = le_condition.fit_transform(X['condition'])

print("\nLocation mapping:", dict(zip(le_location.classes_, le_location.transform(le_location.classes_))))
print("Condition mapping:", dict(zip(le_condition.classes_, le_condition.transform(le_condition.classes_))))

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n=== Model Performance ===")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# Save model and encoders
model_data = {
    'model': model,
    'le_location': le_location,
    'le_condition': le_condition,
    'feature_names': X.columns.tolist(),
    'r2_score': r2,
    'mae': mae,
    'rmse': rmse
}

import os
model_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(model_dir, 'predictor', 'model.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model_data, f)

print(f"\nModel saved to {model_path}")
