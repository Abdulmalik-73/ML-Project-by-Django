# 📚 Complete Project Documentation

## 🎯 Project Overview

**Project Name:** Haramaya House Price Prediction System  
**Purpose:** Machine Learning web application to predict house prices in Haramaya Town, Ethiopia  
**Type:** Full-stack web application with ML integration  
**Repository:** https://github.com/Abdulmalik-73/ML-Project-by-Django

---

## 🗂️ Project Structure

```
haramaya_house_prediction/
├── config/                      # Django project configuration
│   ├── __init__.py             # Python package marker
│   ├── settings.py             # Django settings (database, apps, middleware)
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI configuration for deployment
│
├── core/                        # Core app (homepage, about page)
│   ├── __init__.py
│   ├── admin.py                # Admin panel configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models (empty for now)
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # Core app URL routing
│   └── views.py                # View functions (home, about)
│
├── predictor/                   # Prediction app (ML model)
│   ├── migrations/             # Database migrations
│   │   ├── 0001_initial.py    # Initial migration for PredictionHistory
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                # Admin panel for predictions
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Django forms for prediction input
│   ├── model.pkl               # Trained ML model (RandomForest)
│   ├── models.py               # PredictionHistory database model
│   ├── tests.py                # Unit tests
│   ├── urls.py                 # Predictor app URL routing
│   └── views.py                # View functions (predict, stats, API)
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template (navbar, footer)
│   ├── home.html               # Homepage
│   ├── about.html              # About page
│   ├── predict.html            # Prediction form page
│   ├── result.html             # Prediction result page
│   ├── model_stats.html        # Model statistics page
│   └── error.html              # Error page
│
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── DEPLOYMENT_SUMMARY.md        # Deployment overview
├── haramaya_house_data.csv      # Dataset (50,000 house records)
├── manage.py                    # Django management script
├── Procfile                     # Render deployment process file
├── QUICK_DEPLOY.md              # Quick deployment guide
├── README.md                    # Project documentation
├── RENDER_DEPLOYMENT_GUIDE.md   # Complete deployment guide
├── render.yaml                  # Render configuration file
├── requirements.txt             # Python dependencies
└── train_model.py               # ML model training script
```

---

## 💻 Languages Used

### **Backend Languages:**
1. **Python 3.14**
   - Main programming language
   - Used for: Django framework, ML model, data processing

### **Frontend Languages:**
1. **HTML5**
   - Structure of web pages
   - Used in: All template files (7 templates)

2. **CSS3**
   - Styling and design
   - Used in: Inline styles and Bootstrap customization

3. **JavaScript**
   - Client-side interactivity
   - Used in: Form validation, dynamic content

### **Configuration Languages:**
1. **YAML**
   - render.yaml configuration

2. **Markdown**
   - Documentation files (.md)

---

## 📦 Libraries & Frameworks

### **Backend Libraries:**

#### 1. **Django 4.2.7**
   - **Purpose:** Web framework
   - **Used for:**
     - URL routing
     - Template rendering
     - Database ORM
     - Admin panel
     - Form handling
     - User authentication

#### 2. **pandas 2.1.3**
   - **Purpose:** Data manipulation
   - **Used for:**
     - Loading CSV dataset
     - Data preprocessing
     - Feature engineering
     - Creating DataFrames for ML model

#### 3. **numpy 1.26.2**
   - **Purpose:** Numerical computing
   - **Used for:**
     - Array operations
     - Mathematical calculations
     - ML model input/output

#### 4. **scikit-learn 1.3.2**
   - **Purpose:** Machine Learning
   - **Used for:**
     - RandomForestRegressor (prediction model)
     - LabelEncoder (encoding categorical data)
     - train_test_split (splitting dataset)
     - Model evaluation metrics (R², MAE, RMSE)

#### 5. **matplotlib 3.8.2**
   - **Purpose:** Data visualization
   - **Used for:**
     - Creating charts (optional)
     - Model performance visualization

#### 6. **seaborn 0.13.0**
   - **Purpose:** Statistical visualization
   - **Used for:**
     - Enhanced data visualization
     - Statistical plots

#### 7. **Pillow 10.1.0**
   - **Purpose:** Image processing
   - **Used for:**
     - Image handling (if needed)
     - Django ImageField support

#### 8. **gunicorn 21.2.0**
   - **Purpose:** WSGI HTTP Server
   - **Used for:**
     - Production deployment
     - Serving Django application on Render

#### 9. **whitenoise 6.6.0**
   - **Purpose:** Static file serving
   - **Used for:**
     - Serving CSS, JS, images in production
     - No need for separate static file server

#### 10. **python-decouple 3.8**
   - **Purpose:** Environment variable management
   - **Used for:**
     - Separating settings from code
     - Managing DEBUG, SECRET_KEY, etc.

---

### **Frontend Frameworks:**

#### 1. **Bootstrap 5**
   - **Purpose:** CSS framework
   - **Used for:**
     - Responsive grid system
     - Pre-built components (cards, forms, buttons)
     - Mobile-first design
     - Navigation bar
     - Form styling

#### 2. **Font Awesome**
   - **Purpose:** Icon library
   - **Used for:**
     - Icons throughout the UI
     - Visual enhancement
     - Better UX

---

## 🔧 How Each Library is Used

### **Step-by-Step Usage:**

#### **Step 1: Data Processing (pandas, numpy)**
```python
# train_model.py
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('haramaya_house_data.csv')

# Prepare features
X = df.drop('price', axis=1)
y = df['price']
```

#### **Step 2: Machine Learning (scikit-learn)**
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Encode categorical variables
le_location = LabelEncoder()
X['location'] = le_location.fit_transform(X['location'])

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

#### **Step 3: Model Saving (pickle)**
```python
import pickle

# Save model
model_data = {
    'model': model,
    'le_location': le_location,
    'le_condition': le_condition,
    'r2_score': r2,
    'mae': mae,
    'rmse': rmse
}

with open('predictor/model.pkl', 'wb') as f:
    pickle.dump(model_data, f)
```

#### **Step 4: Web Framework (Django)**
```python
# predictor/views.py
from django.shortcuts import render
from django.views.generic import FormView

class PredictionView(FormView):
    template_name = 'predict.html'
    form_class = HousePredictionForm
    
    def form_valid(self, form):
        # Load model
        model_data = load_model()
        
        # Make prediction
        predicted_price = model.predict(features)[0]
        
        # Render result
        return render(self.request, 'result.html', context)
```

#### **Step 5: Database (Django ORM)**
```python
# predictor/models.py
from django.db import models

class PredictionHistory(models.Model):
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### **Step 6: Forms (Django Forms)**
```python
# predictor/forms.py
from django import forms

class HousePredictionForm(forms.Form):
    bedrooms = forms.IntegerField(min_value=1, max_value=10)
    bathrooms = forms.IntegerField(min_value=1, max_value=10)
    location = forms.ChoiceField(choices=LOCATION_CHOICES)
```

#### **Step 7: Templates (HTML + Bootstrap)**
```html
<!-- templates/predict.html -->
{% extends 'base.html' %}

<div class="container">
    <form method="post" class="needs-validation">
        {% csrf_token %}
        <div class="mb-3">
            {{ form.bedrooms }}
        </div>
        <button type="submit" class="btn btn-primary">
            Predict Price
        </button>
    </form>
</div>
```

#### **Step 8: Static Files (WhiteNoise)**
```python
# config/settings.py
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serves static files
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### **Step 9: Deployment (Gunicorn)**
```bash
# Start command on Render
gunicorn config.wsgi:application
```

---

## 🎯 Complete Development Flow

### **1. Data Collection**
- Created dataset with 50,000 house records
- Features: bedrooms, bathrooms, size, location, condition, year

### **2. Model Training**
- Used RandomForestRegressor
- Achieved 96.36% accuracy (R² score)
- Saved model as pickle file

### **3. Django Setup**
- Created Django project with 2 apps (core, predictor)
- Configured database (SQLite)
- Set up URL routing

### **4. Frontend Development**
- Created 7 HTML templates
- Used Bootstrap 5 for styling
- Added Font Awesome icons

### **5. Integration**
- Connected ML model to Django views
- Created prediction form
- Saved predictions to database

### **6. Deployment Configuration**
- Added Gunicorn for production server
- Configured WhiteNoise for static files
- Created render.yaml for Render deployment

---

## 📊 Model Details

**Algorithm:** Random Forest Regressor  
**Features:** 7 (bedrooms, bathrooms, house_size, land_size, location, condition, year_built)  
**Training Data:** 40,000 samples  
**Test Data:** 10,000 samples  
**Performance:**
- R² Score: 0.9636 (96.36%)
- MAE: 95,097.69 ETB
- RMSE: 124,409.94 ETB

---

## 🌐 Deployment

**Platform:** Render  
**Type:** Web Service  
**Server:** Gunicorn  
**Database:** SQLite (Free tier) / PostgreSQL (Production)  
**Static Files:** WhiteNoise

---

## 📝 Summary

This project uses:
- **1 Backend Language:** Python
- **3 Frontend Languages:** HTML, CSS, JavaScript
- **10 Python Libraries:** Django, pandas, numpy, scikit-learn, matplotlib, seaborn, Pillow, gunicorn, whitenoise, python-decouple
- **2 Frontend Frameworks:** Bootstrap 5, Font Awesome
- **1 ML Algorithm:** Random Forest Regressor
- **1 Database:** SQLite
- **1 Deployment Platform:** Render

**Total Technologies:** 19

---

**Built with ❤️ for Haramaya Town, Eastern Ethiopia**
