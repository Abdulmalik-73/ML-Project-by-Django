# Quick Reference Guide

## 🚀 Getting Started (5 Minutes)

```bash
# 1. Navigate to project
cd haramaya_house_prediction

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train ML model
python train_model.py

# 5. Setup database
python manage.py migrate

# 6. Run server
python manage.py runserver

# 7. Open browser
# http://localhost:8000/
```

## 📍 URLs

| Page | URL |
|------|-----|
| Home | http://localhost:8000/ |
| Predict | http://localhost:8000/predict/ |
| Stats | http://localhost:8000/predict/stats/ |
| About | http://localhost:8000/about/ |
| Admin | http://localhost:8000/admin/ |
| API | http://localhost:8000/predict/api/predict/ |

## 🎯 Main Features

### 1. Home Page
- Welcome message
- Feature overview
- Location information
- Quick links

### 2. Prediction Page
- Form with 7 fields
- Real-time validation
- Model accuracy display

### 3. Results Page
- Predicted price in ETB
- Confidence range (±10%)
- Input summary
- Model metrics

### 4. Model Stats
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- Prediction history count

### 5. About Page
- System explanation
- ML concepts
- Data sources
- Technology stack

## 📝 Form Fields

| Field | Type | Range | Required |
|-------|------|-------|----------|
| Bedrooms | Integer | 1-10 | Yes |
| Bathrooms | Integer | 1-10 | Yes |
| House Size | Float | 30-500 sqm | Yes |
| Land Size | Float | 100-2000 sqm | Yes |
| Location | Dropdown | 6 options | Yes |
| Condition | Dropdown | 3 options | Yes |
| Year Built | Integer | 2000-2025 | Yes |

## 📍 Locations

1. Tinika
2. Harar Gate Area
3. University Area
4. Gende Kore
5. Quncho Ber
6. Kore Hiwot

## 🏠 House Conditions

1. New
2. Good
3. Needs Renovation

## 🔌 API Endpoint

**URL**: `/predict/api/predict/`
**Method**: POST
**Content-Type**: application/json

### Request Example
```json
{
  "bedrooms": 3,
  "bathrooms": 2,
  "house_size": 120,
  "land_size": 500,
  "location": "Tinika",
  "condition": "Good",
  "year_built": 2015
}
```

### Response Example
```json
{
  "success": true,
  "predicted_price": 850000,
  "lower_range": 765000,
  "upper_range": 935000,
  "currency": "ETB"
}
```

## 📊 Model Info

- **Algorithm**: Random Forest Regressor
- **Trees**: 100
- **Max Depth**: 10
- **Training Samples**: 44
- **Test Samples**: 11
- **R² Score**: ~0.95
- **MAE**: ~50,000 ETB

## 📁 Important Files

| File | Purpose |
|------|---------|
| `train_model.py` | Train ML model |
| `haramaya_house_data.csv` | Training dataset |
| `predictor/model.pkl` | Saved model |
| `manage.py` | Django management |
| `requirements.txt` | Dependencies |
| `config/settings.py` | Django settings |

## 🛠️ Common Commands

```bash
# Run server
python manage.py runserver

# Run on different port
python manage.py runserver 8001

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Train model
python train_model.py

# Deactivate virtual environment
deactivate
```

## 🔐 Admin Panel

**URL**: http://localhost:8000/admin/

### Features
- View all predictions
- Filter by location, condition, date
- Search predictions
- View prediction history

### Login
Use superuser credentials created with:
```bash
python manage.py createsuperuser
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | Activate venv, install requirements |
| Model not found | Run `python train_model.py` |
| Port in use | Use `python manage.py runserver 8001` |
| Database error | Run `python manage.py migrate` |
| Admin access denied | Create superuser with `python manage.py createsuperuser` |

## 📚 Documentation Files

- **README.md** - Full documentation
- **SETUP.md** - Quick start guide
- **INSTALLATION.md** - Detailed installation
- **PROJECT_SUMMARY.md** - Feature overview
- **QUICK_REFERENCE.md** - This file

## 🎓 Learning Resources

### In the Application
- About page explains ML concepts
- Model stats page shows metrics
- Form tooltips provide guidance

### External Resources
- Django: https://docs.djangoproject.com/
- scikit-learn: https://scikit-learn.org/
- Bootstrap: https://getbootstrap.com/

## 💡 Tips

1. **Accurate Predictions**: Provide accurate house measurements
2. **Model Training**: Retrain model after adding new data
3. **Admin Access**: Create superuser for admin panel
4. **API Testing**: Use curl or Postman for API testing
5. **Customization**: Edit templates for UI changes

## 🔄 Workflow

1. **Setup** → Install dependencies
2. **Train** → Run `python train_model.py`
3. **Migrate** → Run `python manage.py migrate`
4. **Run** → Start development server
5. **Test** → Make predictions
6. **Customize** → Edit templates/settings as needed

## 📞 Support

For issues:
1. Check troubleshooting section
2. Review README.md
3. Check Django/scikit-learn docs
4. Review error messages carefully

## ✅ Verification

After setup, verify:
- [ ] Home page loads
- [ ] Prediction form works
- [ ] Results display correctly
- [ ] Admin panel accessible
- [ ] API endpoint responds
- [ ] Model stats show metrics

---

**Ready to predict house prices! 🏠📊**
