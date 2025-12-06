# 🚀 How to Run the Project

## 📁 IMPORTANT: Open Terminal in the Correct Folder

**You MUST open your terminal in the `haramaya_house_prediction` folder!**

### How to Open Terminal in the Right Folder:

**Option 1: Using File Explorer (Windows)**
1. Navigate to: `C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction`
2. Click in the address bar and type `cmd` then press Enter
3. Terminal will open in the correct folder

**Option 2: Using Command Prompt**
```bash
cd "C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction"
```

**Option 3: Using VS Code**
1. Open the `haramaya_house_prediction` folder in VS Code
2. Open Terminal (Ctrl + `)
3. Terminal automatically opens in the correct folder

---

## Method 1: Using run.py (Django - Recommended)

**In the `haramaya_house_prediction` folder, run:**
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

## Method 2: Using streamlit.py (Simple UI)

**In the `haramaya_house_prediction` folder:**

First install Streamlit:
```bash
pip install streamlit
```

Then run:
```bash
streamlit run streamlit.py
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
