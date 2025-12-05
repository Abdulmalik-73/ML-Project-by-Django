import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 50,000 records
n_records = 50000

locations = ['Tinika', 'Harar_gate_area', 'University_area', 'Gende_Kore', 'Quncho_Ber', 'Kore_Hiwot']
conditions = ['New', 'Good', 'Needs_Renovation']

data = {
    'bedrooms': np.random.randint(1, 6, n_records),
    'bathrooms': np.random.randint(1, 5, n_records),
    'house_size': np.random.uniform(70, 250, n_records),
    'land_size': np.random.uniform(250, 1000, n_records),
    'location': np.random.choice(locations, n_records),
    'condition': np.random.choice(conditions, n_records),
    'year_built': np.random.randint(2008, 2023, n_records),
}

# Generate prices based on features (realistic pricing model)
df = pd.DataFrame(data)
base_price = 300000
price = (
    base_price +
    df['bedrooms'] * 150000 +
    df['bathrooms'] * 100000 +
    df['house_size'] * 3000 +
    df['land_size'] * 500 +
    (df['year_built'] - 2008) * 20000 +
    np.random.normal(0, 50000, n_records)
)

# Adjust by location
location_multiplier = {
    'Tinika': 1.0,
    'Harar_gate_area': 1.15,
    'University_area': 1.25,
    'Gende_Kore': 0.9,
    'Quncho_Ber': 1.35,
    'Kore_Hiwot': 0.85
}
price = price * df['location'].map(location_multiplier)

# Adjust by condition
condition_multiplier = {
    'New': 1.2,
    'Good': 1.0,
    'Needs_Renovation': 0.7
}
price = price * df['condition'].map(condition_multiplier)

df['price'] = np.maximum(price, 200000).astype(int)

# Save to CSV
df.to_csv('haramaya_house_data.csv', index=False)
print(f'✅ Generated {len(df):,} records')
print(f'Price range: {df["price"].min():,} - {df["price"].max():,} ETB')
print(f'Average price: {df["price"].mean():,.0f} ETB')
print(f'Dataset saved to haramaya_house_data.csv')
