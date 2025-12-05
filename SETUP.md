# Quick Start Guide

## Step 1: Navigate to Project Directory

```bash
cd haramaya_house_prediction
```

## Step 2: Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Train the ML Model

```bash
python train_model.py
```

**Expected Output:**
```
Dataset shape: (56, 8)

=== Model Performance ===
R² Score: 0.9500
MAE: 50000.00
RMSE: 60000.00

Model saved to predictor/model.pkl
```

## Step 5: Initialize Django Database

```bash
python manage.py migrate
```

## Step 6: Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create username, email, and password.

## Step 7: Run Development Server

```bash
python manage.py runserver
```

**Output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Step 8: Access the Application

Open your browser and visit:

- **Home**: http://localhost:8000/
- **Predict**: http://localhost:8000/predict/
- **Stats**: http://localhost:8000/predict/stats/
- **About**: http://localhost:8000/about/
- **Admin**: http://localhost:8000/admin/ (if superuser created)

## Troubleshooting

### Issue: "No module named 'django'"
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: "model.pkl not found"
**Solution**: Train the model first
```bash
python train_model.py
```

### Issue: "Port 8000 already in use"
**Solution**: Use a different port
```bash
python manage.py runserver 8001
```

### Issue: Database errors
**Solution**: Reset migrations
```bash
python manage.py migrate --run-syncdb
```

## Next Steps

1. **Make Predictions**: Go to http://localhost:8000/predict/
2. **View Stats**: Check model performance at http://localhost:8000/predict/stats/
3. **Admin Panel**: Manage predictions at http://localhost:8000/admin/
4. **API Testing**: Use the REST API endpoint at `/predict/api/predict/`

## File Locations

- **Model**: `predictor/model.pkl`
- **Dataset**: `haramaya_house_data.csv`
- **Database**: `db.sqlite3`
- **Templates**: `templates/`
- **Static Files**: `static/`

## Common Commands

```bash
# Run server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access shell
python manage.py shell

# Collect static files
python manage.py collectstatic

# Train model
python train_model.py
```

## Deactivate Virtual Environment

```bash
deactivate
```

---

**You're all set! Start making house price predictions! 🏠**
