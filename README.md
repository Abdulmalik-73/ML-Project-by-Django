# Haramaya House Price Prediction System

A complete Django web application with Machine Learning for predicting house prices in Haramaya Town, Eastern Ethiopia.

## 🎯 Features

- ✅ **Machine Learning Model** - Random Forest Regressor (96.65% accuracy)
- ✅ **Web Interface** - Modern, responsive UI with Bootstrap 5
- ✅ **Price Predictions** - Accurate predictions with confidence ranges
- ✅ **Model Statistics** - View model performance metrics
- ✅ **Prediction History** - Track all predictions in admin panel
- ✅ **REST API** - JSON endpoint for programmatic predictions
- ✅ **Admin Dashboard** - Manage predictions and view statistics

## 📁 Project Structure

```
haramaya_house_prediction/
├── config/                    # Django configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                      # Core app (homepage, about)
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── predictor/                 # Prediction app (ML model)
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── model.pkl              # Trained ML model
├── templates/                 # HTML templates (7 files)
│   ├── base.html
│   ├── home.html
│   ├── predict.html
│   ├── result.html
│   ├── about.html
│   ├── model_stats.html
│   └── error.html
├── haramaya_house_data.csv    # Dataset (50,000 records)
├── train_model.py             # Model training script
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

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

### 3. Train the Model
```bash
python train_model.py
```

### 4. Setup Database
```bash
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000/**

## 📊 Dataset

- **Records**: 50,000 houses
- **Price Range**: 608,998 - 4,682,736 ETB
- **Average Price**: 2,026,113 ETB
- **Features**: 7 (bedrooms, bathrooms, house_size, land_size, location, condition, year_built)
- **Locations**: 6 (Tinika, Harar Gate, University Area, Gende Kore, Quncho Ber, Kore Hiwot)
- **Conditions**: 3 (New, Good, Needs Renovation)

## 🤖 Model Performance

- **Algorithm**: Random Forest Regressor
- **R² Score**: 0.9665 (96.65% accuracy)
- **MAE**: 94,207.58 ETB
- **RMSE**: 120,665.92 ETB
- **Training Samples**: 40,000
- **Test Samples**: 10,000

## 🌐 Available Endpoints

| Endpoint | URL |
|----------|-----|
| Home | http://localhost:8000/ |
| Predict | http://localhost:8000/predict/ |
| Stats | http://localhost:8000/predict/stats/ |
| About | http://localhost:8000/about/ |
| Admin | http://localhost:8000/admin/ |
| API | http://localhost:8000/predict/api/predict/ |

## 🔌 API Usage

### Request
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

### Response
```json
{
  "success": true,
  "predicted_price": 2000000,
  "lower_range": 1800000,
  "upper_range": 2200000,
  "currency": "ETB"
}
```

## 🛠️ Technology Stack

**Backend**: Python 3, Django 5.2.8, scikit-learn, pandas, numpy
**Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, Font Awesome
**Database**: SQLite3
**ML Model**: Random Forest Regressor

## 📝 Making Predictions

1. Go to **Predict Price** page
2. Fill in house details:
   - Bedrooms (1-5)
   - Bathrooms (1-4)
   - House Size (70-250 sqm)
   - Land Size (250-1000 sqm)
   - Location (select from 6 options)
   - Condition (New, Good, Needs Renovation)
   - Year Built (2008-2023)
3. Click **Predict Price**
4. View results with confidence range

## 🔐 Admin Panel

Access at: http://localhost:8000/admin/

- View all predictions
- Filter by location, condition, date
- Search predictions
- Track prediction history

## 🎓 Haramaya Town Locations

- **Tinika** - Residential area with good infrastructure
- **Harar Gate Area** - Commercial and residential hub
- **University Area** - Modern facilities near Haramaya University
- **Gende Kore** - Growing residential neighborhood
- **Quncho Ber** - Premium residential area
- **Kore Hiwot** - Developing area with growth potential

## 🏠 House Conditions

- **New** - Recently built, excellent condition
- **Good** - Well-maintained, minor wear
- **Needs Renovation** - Requires repairs/updates

## 🔄 Customization

### Add More Training Data
1. Edit `haramaya_house_data.csv`
2. Add new rows with house data
3. Run `python train_model.py` to retrain

### Change Model Algorithm
Edit `train_model.py` and replace RandomForestRegressor with your preferred algorithm

### Modify UI
Edit templates in `templates/` folder

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Run `python train_model.py` |
| Port in use | Run `python manage.py runserver 8001` |
| Database error | Run `python manage.py migrate --run-syncdb` |

## 📄 License

Open source for educational purposes.

## ⚠️ Disclaimer

This prediction system is for informational purposes only. Actual house prices may vary based on market conditions, negotiations, and other factors. Always consult with real estate professionals for accurate valuations.

---

**Built with Python, Django, and Machine Learning**
**Haramaya Town, Eastern Ethiopia**
