# 🚀 Deploy to Render - Complete Step-by-Step Guide

## ✅ Prerequisites
- GitHub account with your project pushed ✓
- Render account (free at https://render.com)

---

## 📋 STEP 1: Create Render Account

1. Go to **https://render.com**
2. Click **"Get Started"** or **"Sign Up"**
3. Choose **"Sign up with GitHub"** (recommended)
4. Authorize Render to access your GitHub account
5. You'll be redirected to Render Dashboard

---

## 📋 STEP 2: Connect GitHub Repository

1. In Render Dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. If this is your first time:
   - Click **"Configure account"**
   - Select your GitHub account
   - Choose **"All repositories"** or select **"ML-Project-by-Django"**
   - Click **"Install"**
5. Search for **"ML-Project-by-Django"**
6. Click **"Connect"** next to your repository

---

## 📋 STEP 3: Configure Web Service

Fill in these settings:

### Basic Settings:
| Field | Value |
|-------|-------|
| **Name** | `haramaya-house-prediction` |
| **Region** | `Oregon` (or closest to you) |
| **Branch** | `main` |
| **Root Directory** | `haramaya_house_prediction` |
| **Runtime** | `Python 3` |

### Build & Start Commands:

**Build Command:**
```bash
pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && python train_model.py
```

**Start Command:**
```bash
gunicorn config.wsgi:application
```

### Instance Type:
- Select **"Free"** (for testing)
- Or **"Starter"** ($7/month for better performance)

---

## 📋 STEP 4: Add Environment Variables

Scroll down to **"Environment Variables"** section and add these:

### Variable 1: DEBUG
- **Key:** `DEBUG`
- **Value:** `False`
- Click **"Add"**

### Variable 2: SECRET_KEY
- **Key:** `SECRET_KEY`
- **Value:** `django-insecure-haramaya-house-prediction-render-2025-secret-key`
- Click **"Add"**

**Note:** For production, generate a secure key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Variable 3: ALLOWED_HOSTS
- **Key:** `ALLOWED_HOSTS`
- **Value:** `localhost,127.0.0.1,.onrender.com`
- Click **"Add"**

### Variable 4: PYTHON_VERSION
- **Key:** `PYTHON_VERSION`
- **Value:** `3.11.0`
- Click **"Add"**

---

## 📋 STEP 5: Deploy!

1. Review all settings
2. Click **"Create Web Service"** button at the bottom
3. Render will start building your project
4. **Wait 5-10 minutes** for deployment to complete
5. Watch the build logs for any errors

### Build Process:
- ✅ Installing dependencies
- ✅ Running migrations
- ✅ Collecting static files
- ✅ Training ML model
- ✅ Starting server

---

## 📋 STEP 6: Verify Deployment

Once deployment is complete:

1. You'll see a URL like: `https://haramaya-house-prediction.onrender.com`
2. Click the URL to visit your deployed app
3. Test these pages:
   - **Home:** `/`
   - **Predict:** `/predict/`
   - **About:** `/about/`
   - **Stats:** `/predict/stats/`

---

## 🔧 STEP 7: Troubleshooting

### If deployment fails:

1. **Check Build Logs:**
   - Click **"Logs"** tab in Render dashboard
   - Look for red error messages
   - Common issues:
     - Missing dependencies in `requirements.txt`
     - Incorrect build command
     - Database migration errors

2. **Common Fixes:**

   **Issue:** `ModuleNotFoundError`
   - **Fix:** Add missing package to `requirements.txt`

   **Issue:** `SECRET_KEY not set`
   - **Fix:** Verify environment variable is added

   **Issue:** `Static files not found`
   - **Fix:** Ensure `collectstatic` is in build command

   **Issue:** `Model not found`
   - **Fix:** Ensure `train_model.py` is in build command

3. **Manual Redeploy:**
   - Click **"Manual Deploy"** button
   - Select **"Clear build cache & deploy"**
   - Wait for build to complete

---

## 📋 STEP 8: Update Your Deployed App

To deploy updates after making changes:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. Render automatically redeploys (if auto-deploy is enabled)
4. Check deployment status in Render dashboard

---

## 📋 STEP 9: Enable Auto-Deploy (Optional)

1. Go to your service in Render dashboard
2. Click **"Settings"** tab
3. Scroll to **"Build & Deploy"**
4. Enable **"Auto-Deploy"**
5. Now every push to `main` branch will trigger deployment

---

## 📋 STEP 10: Custom Domain (Optional)

To use your own domain:

1. In Render dashboard, go to your service
2. Click **"Settings"** tab
3. Scroll to **"Custom Domain"**
4. Click **"Add Custom Domain"**
5. Enter your domain (e.g., `haramaya-prediction.com`)
6. Follow DNS configuration instructions
7. Update `ALLOWED_HOSTS` environment variable to include your domain

---

## 🌐 Your Deployed URLs

Once live, you can access:

- **Home:** `https://haramaya-house-prediction.onrender.com/`
- **Predict:** `https://haramaya-house-prediction.onrender.com/predict/`
- **Stats:** `https://haramaya-house-prediction.onrender.com/predict/stats/`
- **About:** `https://haramaya-house-prediction.onrender.com/about/`
- **Admin:** `https://haramaya-house-prediction.onrender.com/admin/`
- **API:** `https://haramaya-house-prediction.onrender.com/predict/api/predict/`

---

## ⚠️ Important Notes

### Free Plan Limitations:
- Spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Limited resources (512 MB RAM)
- Good for testing and demos

### Production Recommendations:
- Use **Starter** plan or higher ($7/month)
- Set up PostgreSQL database (instead of SQLite)
- Use environment variables for all sensitive data
- Enable auto-deploy from GitHub
- Set up monitoring and alerts
- Regular backups

### Database Note:
- Free plan uses SQLite (file-based)
- For production, upgrade to PostgreSQL:
  1. Add PostgreSQL database in Render
  2. Update `DATABASE_URL` environment variable
  3. Update `settings.py` to use PostgreSQL

---

## 📞 Support

- **Render Docs:** https://render.com/docs
- **Django Docs:** https://docs.djangoproject.com/
- **Your Repository:** https://github.com/Abdulmalik-73/ML-Project-by-Django

---

## ✅ Deployment Checklist

Before deploying, ensure:

- [x] All code pushed to GitHub
- [x] `requirements.txt` has all dependencies
- [x] `Procfile` exists (optional, using render.yaml)
- [x] `render.yaml` configured correctly
- [x] Environment variables ready
- [x] Model training script works locally
- [x] Database migrations created
- [x] Static files configured

---

## 🎉 That's It!

Your Haramaya House Price Prediction app is now live on the internet!

**Share your deployed URL with anyone in the world!** 🌍

---

**Built with Python, Django, and Machine Learning**
**Deployed on Render**
**Haramaya Town, Eastern Ethiopia**
