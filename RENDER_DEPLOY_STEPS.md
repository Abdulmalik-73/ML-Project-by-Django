# Complete Render Deployment - Step by Step

## Prerequisites
✅ GitHub account with repository pushed
✅ Project files ready
✅ All configuration files in place

---

## STEP 1: Go to Render Dashboard

1. Open https://render.com
2. Sign in with your GitHub account
3. You should see your dashboard

---

## STEP 2: Create New Web Service

1. Click the **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect a repository"**

---

## STEP 3: Connect Your GitHub Repository

1. Search for: `ML-Project-by-Django`
2. Click **"Connect"** next to your repository
3. You'll be redirected to the service creation page

---

## STEP 4: Configure Basic Settings

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `haramaya-house-prediction` |
| **Environment** | `Python 3` |
| **Region** | `Oregon` (or your preferred region) |
| **Branch** | `main` |
| **Root Directory** | Leave **EMPTY** |

---

## STEP 5: Set Build and Start Commands

### Build Command
Copy and paste exactly:
```
pip install -r haramaya_house_prediction/requirements.txt && python haramaya_house_prediction/manage.py migrate && python haramaya_house_prediction/manage.py collectstatic --noinput
```

### Start Command
Copy and paste exactly:
```
gunicorn config.wsgi:application --chdir haramaya_house_prediction
```

---

## STEP 6: Add Environment Variables

Scroll down to **"Environment"** section and click **"Add Environment Variable"**

Add these variables one by one:

### Variable 1: DEBUG
- **Key**: `DEBUG`
- **Value**: `False`
- Click **"Add"**

### Variable 2: SECRET_KEY
- **Key**: `SECRET_KEY`
- **Value**: Copy this (or generate your own):
  ```
  django-insecure-haramaya-house-prediction-render-deployment-2025
  ```
- Click **"Add"**

### Variable 3: ALLOWED_HOSTS
- **Key**: `ALLOWED_HOSTS`
- **Value**: `localhost,127.0.0.1,.onrender.com`
- Click **"Add"**

### Variable 4: PYTHON_VERSION
- **Key**: `PYTHON_VERSION`
- **Value**: `3.11.0`
- Click **"Add"**

---

## STEP 7: Select Plan

- Choose **"Free"** plan (for testing)
- Or **"Starter"** plan ($7/month) for better performance

---

## STEP 8: Deploy

1. Click **"Create Web Service"** button
2. Render will start building your project
3. **Wait 5-10 minutes** for deployment to complete
4. You'll see a URL like: `https://haramaya-house-prediction.onrender.com`

---

## STEP 9: Verify Deployment

Once deployment is complete:

1. Click the URL to visit your app
2. You should see the **Home Page**
3. Test these pages:
   - **Home**: `/` ✓
   - **Predict**: `/predict/` ✓
   - **About**: `/about/` ✓
   - **Stats**: `/predict/stats/` ✓

---

## STEP 10: Troubleshooting

### If deployment fails:

1. **Check Build Logs**
   - Click **"Logs"** tab in Render dashboard
   - Look for red error messages
   - Copy the error and share with me

2. **Common Issues & Fixes**

   | Issue | Fix |
   |-------|-----|
   | `ModuleNotFoundError` | Check requirements.txt has all packages |
   | `SECRET_KEY not set` | Verify environment variable is added |
   | `Static files not found` | Run `collectstatic` command (already in build) |
   | `Database error` | Migrations should run automatically |

3. **Manual Redeploy**
   - Click **"Manual Deploy"** button
   - Select **"Deploy latest commit"**
   - Wait for build to complete

---

## STEP 11: Update Your Project (After Deployment)

To deploy updates:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```
3. Render automatically redeploys (if auto-deploy enabled)
4. Check deployment status in Render dashboard

---

## STEP 12: Access Your Deployed App

Once live, you can access:

- **Home**: `https://haramaya-house-prediction.onrender.com/`
- **Predict**: `https://haramaya-house-prediction.onrender.com/predict/`
- **Stats**: `https://haramaya-house-prediction.onrender.com/predict/stats/`
- **About**: `https://haramaya-house-prediction.onrender.com/about/`
- **Admin**: `https://haramaya-house-prediction.onrender.com/admin/`
- **API**: `https://haramaya-house-prediction.onrender.com/predict/api/predict/`

---

## Important Notes

### Free Plan Limitations
- Spins down after 15 minutes of inactivity
- Limited resources
- Good for testing/demo

### Production Recommendations
- Use **Starter** or higher plan for production
- Set up PostgreSQL database (instead of SQLite)
- Enable auto-deploy from GitHub
- Monitor application logs regularly

### If You Need Help
- Check Render Logs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com/
- Share error messages with me

---

## Quick Reference

**Your Repository**: https://github.com/Abdulmalik-73/ML-Project-by-Django

**Render Dashboard**: https://dashboard.render.com

**Your App URL** (after deployment): `https://haramaya-house-prediction.onrender.com`

---

**Follow these steps exactly and your app will be live! 🚀**
