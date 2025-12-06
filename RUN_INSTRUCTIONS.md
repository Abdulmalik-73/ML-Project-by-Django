# 🚀 How to Run the Project

## Method 1: Using run.py (Django - Recommended)

Simply run:
```bash
python run.py
```

This will:
- ✅ Run database migrations
- ✅ Collect static files
- ✅ Start the Django development server

Then open your browser and visit:
- **Home**: http://127.0.0.1:8000/
- **Predict**: http://127.0.0.1:8000/predict/
- **About**: http://127.0.0.1:8000/about/

---

## Method 2: Using Streamlit (Simple UI)

First install Streamlit:
```bash
pip install streamlit
```

Then run:
```bash
streamlit run streamlit_app.py
```

This will open a simpler, cleaner interface in your browser automatically.

---

## Method 3: Traditional Django Way

```bash
python manage.py migrate
python manage.py runserver
```

---

## First Time Setup

If this is your first time running the project:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model (if not already trained):**
   ```bash
   python train_model.py
   ```

3. **Run the server:**
   ```bash
   python run.py
   ```

---

## Troubleshooting

### Missing Dependencies
If you get import errors, install missing packages:
```bash
pip install django whitenoise python-decouple gunicorn
```

### Model Not Found
If you see "Model not found" error:
```bash
python train_model.py
```

### Port Already in Use
If port 8000 is busy, specify a different port:
```bash
python manage.py runserver 8080
```

---

## Quick Commands

| Command | Description |
|---------|-------------|
| `python run.py` | Start Django server (easiest) |
| `streamlit run streamlit_app.py` | Start Streamlit UI |
| `python train_model.py` | Train/retrain the ML model |
| `python manage.py migrate` | Run database migrations |
| `python manage.py createsuperuser` | Create admin user |

---

**Enjoy predicting house prices! 🏠💰**
