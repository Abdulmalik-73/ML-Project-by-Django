# ⚡ QUICK START GUIDE

## 🎯 Easiest Way to Run (Windows)

### Option 1: Double-Click to Run Django Server
1. Navigate to the `haramaya_house_prediction` folder
2. **Double-click** `START_SERVER.bat`
3. Server will start automatically!
4. Open browser: http://127.0.0.1:8000/

### Option 2: Double-Click to Run Streamlit UI
1. Navigate to the `haramaya_house_prediction` folder
2. **Double-click** `START_STREAMLIT.bat`
3. Streamlit UI will open in your browser automatically!

---

## 💻 Using Terminal/Command Prompt

### Step 1: Open Terminal in the Correct Folder

**IMPORTANT:** You must be in the `haramaya_house_prediction` folder!

**Your project path:**
```
C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction
```

**How to get there:**

**Method A: File Explorer**
1. Open File Explorer
2. Navigate to: `C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction`
3. Click in the address bar
4. Type `cmd` and press Enter
5. Terminal opens in the correct folder ✅

**Method B: Command Prompt**
```bash
cd "C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction"
```

**Method C: PowerShell**
```powershell
cd "C:\Users\nurea\Desktop\Python Django project\haramaya_house_prediction"
```

---

### Step 2: Run the Project

**Option A: Django Server (Full Features)**
```bash
python run.py
```
Then visit: http://127.0.0.1:8000/

**Option B: Streamlit UI (Simple & Clean)**
```bash
streamlit run streamlit.py
```
Browser opens automatically!

---

## 📂 Folder Structure

```
Python Django project/
└── haramaya_house_prediction/    ← YOU MUST BE HERE!
    ├── run.py                     ← Run Django server
    ├── streamlit.py               ← Run Streamlit UI
    ├── START_SERVER.bat           ← Double-click to start Django
    ├── START_STREAMLIT.bat        ← Double-click to start Streamlit
    ├── manage.py
    ├── config/
    ├── core/
    ├── predictor/
    └── templates/
```

---

## ✅ Quick Test

To verify you're in the correct folder, run:
```bash
dir
```

You should see these files:
- `run.py`
- `streamlit.py`
- `manage.py`
- `START_SERVER.bat`
- `START_STREAMLIT.bat`

If you don't see these files, you're in the wrong folder!

---

## 🆘 Troubleshooting

### "python is not recognized"
Install Python from: https://www.python.org/downloads/

### "No module named 'django'"
```bash
pip install django whitenoise python-decouple
```

### "Model not found"
```bash
python train_model.py
```

### Port 8000 already in use
```bash
python manage.py runserver 8080
```

---

## 🎉 That's It!

**Easiest way:** Just double-click `START_SERVER.bat` in the `haramaya_house_prediction` folder!

**Terminal way:** 
1. Open terminal in `haramaya_house_prediction` folder
2. Run `python run.py`
3. Visit http://127.0.0.1:8000/

Enjoy! 🏠💰
