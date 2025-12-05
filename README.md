# Haramaya House Price Prediction System

A complete Django web application with Machine Learning for predicting house prices in Haramaya Town, Eastern Ethiopia.

## Features

✅ **Machine Learning Model** - Random Forest Regressor trained on house data
✅ **Web Interface** - Modern, responsive UI with Bootstrap 5
✅ **Price Predictions** - Accurate predictions with confidence ranges
✅ **Model Statistics** - View model performance metrics
✅ **Prediction History** - Track all predictions in admin panel
✅ **REST API** - JSON endpoint for programmatic predictions
✅ **Admin Dashboard** - Manage predictions and view statistics

## Project Structure

```
haramaya_house_prediction/
├── config/                 # Django configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI application
├── core/                  # Core app (homepage, about)
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── predictor/             # Prediction app (ML model)
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── model.pkl          # Trained model (generated)
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── predict.html
│   ├── result.html
│   ├── about.html
│   ├── model_stats.html
│   └── error.html
├── static/                # Static files (CSS, JS, images)
├── haramaya_house_data.csv # Training dataset
├── train_model.py         # Model training script
├── manage.py              # Django management
└── requirements.txt       # Python dependencies
```

## Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Machine Learning Model

```bash
python train_model.py
```

This will:
- Load the dataset from `haramaya_house_data.csv`
- Train a Random Forest model
- Save the model to `predictor/model.pkl`
- Display model performance metrics

### 4. Setup Django Database

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional - for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000

## Usage

### Web Interface

1. **Home Page** - Overview and quick links
2. **Predict Price** - Fill form with house details and get prediction
3. **Model Stats** - View model performance metrics
4. **About** - Learn about the system and ML concepts

### Making Predictions

1. Go to "Predict Price" page
2. Fill in house details:
   - Number of bedrooms (1-10)
   - Number of bathrooms (1-10)
   - House size in sqm (30-500)
   - Land size in sqm (100-2000)
   - Location (select from dropdown)
   - House condition (New, Good, Needs Renovation)
   - Year built (2000-2025)
3. Click "Predict Price"
4. View results with confidence range

### API Usage

Make POST request to `/predict/api/predict/` with JSON data:

```bash
curl -X POST http://localhost:8000/predict/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "bedrooms": 3,
    "bathrooms": 2,
    "house_size": 120,
    "land_size": 500,
    "location": "Tinika",
    "condition": "Good",
    "year_built": 2015
  }'
```

Response:
```json
{
  "success": true,
  "predicted_price": 850000,
  "lower_range": 765000,
  "upper_range": 935000,
  "currency": "ETB"
}
```

### Admin Panel

Access at: http://localhost:8000/admin

- View all predictions
- Filter by location, condition, date
- Search predictions
- View model statistics

## Haramaya Town Locations

The system supports predictions for these locations:

- **Tinika** - Residential area with good infrastructure
- **Harar Gate Area** - Commercial and residential hub
- **University Area** - Modern facilities near Haramaya University
- **Gende Kore** - Growing residential neighborhood
- **Quncho Ber** - Premium residential area
- **Kore Hiwot** - Developing area with growth potential

## House Conditions

- **New** - Recently built, excellent condition
- **Good** - Well-maintained, minor wear
- **Needs Renovation** - Requires repairs/updates

## Model Performance

The trained model achieves:
- **R² Score**: ~0.95 (95% variance explained)
- **MAE**: ~50,000 ETB (average error)
- **RMSE**: ~60,000 ETB

## Dataset

- **Size**: 56 house records
- **Features**: 7 (bedrooms, bathrooms, house_size, land_size, location, condition, year_built)
- **Target**: Price in ETB
- **Price Range**: 380,000 - 1,600,000 ETB
- **Years**: 2008-2022

## Technology Stack

**Backend:**
- Python 3
- Django 4.2
- scikit-learn (ML)
- pandas (Data processing)
- numpy (Numerical computing)

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome Icons

**Database:**
- SQLite (default)

## Customization

### Add More Training Data

1. Edit `haramaya_house_data.csv`
2. Add new rows with house data
3. Run `python train_model.py` to retrain

### Change Model Algorithm

Edit `train_model.py`:
```python
# Replace RandomForestRegressor with:
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

### Modify UI

Edit templates in `templates/` folder:
- `base.html` - Main layout
- `home.html` - Homepage
- `predict.html` - Prediction form
- `result.html` - Results page

## Troubleshooting

### Model Not Found Error

```bash
python train_model.py
```

### Port Already in Use

```bash
python manage.py runserver 8001
```

### Database Errors

```bash
python manage.py migrate --run-syncdb
```

## Disclaimer

This prediction system is for informational purposes only. Actual house prices may vary based on market conditions, negotiations, and other factors. Always consult with real estate professionals for accurate valuations.

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the About page in the application for more information about how the system works.

---

**Built with ❤️ for Haramaya Town**
