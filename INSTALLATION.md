# Complete Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

## Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd haramaya_house_prediction
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2.7
- pandas 2.1.3
- numpy 1.26.2
- scikit-learn 1.3.2
- matplotlib 3.8.2
- seaborn 0.13.0
- Pillow 10.1.0

### Step 5: Train the Machine Learning Model

```bash
python train_model.py
```

**Expected Output:**
```
Dataset shape: (56, 8)

First few rows:
   bedrooms  bathrooms  house_size  land_size location condition  year_built   price
0         3          2         120        500   Tinika      Good        2015  850000
1         4          3         150        600  Harar_gate_area    New        2020 1200000
...

Location mapping: {'Tinika': 0, 'Harar_gate_area': 1, 'University_area': 2, 'Gende_Kore': 3, 'Quncho_Ber': 4, 'Kore_Hiwot': 5}
Condition mapping: {'Good': 0, 'Needs_Renovation': 1, 'New': 2}

=== Model Performance ===
R² Score: 0.9500
MAE: 50000.00
RMSE: 60000.00

Model saved to predictor/model.pkl
```

### Step 6: Initialize Django Database

```bash
python manage.py migrate
```

**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, predictor
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying predictor.0001_initial... OK
```

### Step 7: Create Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

**Expected Output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 05, 2025 - 19:30:00
Django version 4.2.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 9: Access the Application

Open your web browser and visit:

- **Home Page**: http://localhost:8000/
- **Predict Price**: http://localhost:8000/predict/
- **Model Statistics**: http://localhost:8000/predict/stats/
- **About Page**: http://localhost:8000/about/
- **Admin Panel**: http://localhost:8000/admin/ (use superuser credentials)

## Verification Checklist

After installation, verify everything works:

- [ ] Home page loads with hero section
- [ ] Navigation bar displays all links
- [ ] Prediction form loads with all fields
- [ ] Can submit prediction form
- [ ] Results page shows predicted price
- [ ] Model stats page displays metrics
- [ ] About page loads with information
- [ ] Admin panel accessible with superuser login
- [ ] API endpoint responds to POST requests

## Testing the API

Open a terminal and test the API endpoint:

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

Expected response:
```json
{
  "success": true,
  "predicted_price": 850000.0,
  "lower_range": 765000.0,
  "upper_range": 935000.0,
  "currency": "ETB"
}
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: [Errno 2] No such file or directory: 'predictor/model.pkl'"

**Solution**: Train the model first
```bash
python train_model.py
```

### Issue: "Port 8000 already in use"

**Solution**: Use a different port
```bash
python manage.py runserver 8001
```

### Issue: "django.db.utils.OperationalError: no such table"

**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: "No module named 'rest_framework'"

**Solution**: Install missing package
```bash
pip install djangorestframework
```

### Issue: Model predictions seem inaccurate

**Solution**: Retrain the model with more data
1. Add more records to `haramaya_house_data.csv`
2. Run `python train_model.py`

## Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Restarting the Application

To restart the application later:

1. Activate virtual environment:
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. Run server:
   ```bash
   python manage.py runserver
   ```

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in `config/settings.py`
2. Change `SECRET_KEY` to a secure random string
3. Set `ALLOWED_HOSTS` to your domain
4. Use a production database (PostgreSQL recommended)
5. Use a production web server (Gunicorn, uWSGI)
6. Use a reverse proxy (Nginx, Apache)
7. Enable HTTPS/SSL
8. Collect static files: `python manage.py collectstatic`

## Next Steps

1. Read the [README.md](README.md) for detailed documentation
2. Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for feature overview
3. Explore the admin panel at http://localhost:8000/admin/
4. Make test predictions to verify the model
5. Customize the application as needed

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the README.md file
3. Check Django documentation: https://docs.djangoproject.com/
4. Check scikit-learn documentation: https://scikit-learn.org/

---

**Installation Complete! 🎉**

You're ready to start making house price predictions for Haramaya Town!
