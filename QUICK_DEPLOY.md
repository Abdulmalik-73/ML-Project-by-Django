# ⚡ Quick Deploy to Render (5 Minutes)

## 🎯 Super Fast Deployment

### Step 1: Go to Render
👉 **https://render.com** → Sign up with GitHub

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect **"ML-Project-by-Django"** repository
3. Click **"Connect"**

### Step 3: Fill Settings

**Name:** `haramaya-house-prediction`

**Root Directory:** `haramaya_house_prediction`

**Build Command:**
```bash
pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && python train_model.py
```

**Start Command:**
```bash
gunicorn config.wsgi:application
```

### Step 4: Add Environment Variables

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | `django-insecure-haramaya-house-prediction-render-2025-secret-key` |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1,.onrender.com` |
| `PYTHON_VERSION` | `3.11.0` |

### Step 5: Deploy
Click **"Create Web Service"** → Wait 5-10 minutes → Done! 🎉

---

## 🌐 Your Live URL
`https://haramaya-house-prediction.onrender.com`

---

## 📖 Need More Details?
See **RENDER_DEPLOYMENT_GUIDE.md** for complete step-by-step instructions.

---

**That's it! Your app is live on the internet!** 🚀
