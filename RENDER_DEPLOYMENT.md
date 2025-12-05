# Deploy to Render - Step by Step Guide

## Prerequisites
- GitHub account with your project pushed
- Render account (free at https://render.com)

---

## Step 1: Create Render Account

1. Go to https://render.com
2. Click "Sign up"
3. Sign up with GitHub (recommended)
4. Authorize Render to access your GitHub account

---

## Step 2: Connect GitHub Repository

1. Log in to Render dashboard
2. Click "New +" button
3. Select "Web Service"
4. Click "Connect a repository"
5. Search for "ML-Project-by-Django"
6. Click "Connect"

---

## Step 3: Configure Web Service

### Basic Settings
- **Name**: `haramaya-house-prediction`
- **Environment**: `Python 3`
- **Region**: `Oregon` (or your preferred region)
- **Branch**: `main`
- **Root Directory**: Leave empty (or set to `haramaya_house_prediction` if needed)

### Build Command
```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

### Start Command
```
gunicorn config.wsgi:application
```

### Plan
- Select **Free** plan (for testing)
- Or **Starter** plan for production

---

## Step 4: Set Environment Variables

1. Scroll down to "Environment"
2. Click "Add Environment Variable"
3. Add the following variables:

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | Generate a secure key (use Django secret key generator) |
| `ALLOWED_HOSTS` | `yourdomain.onrender.com,localhost` |
| `PYTHON_VERSION` | `3.11.0` |

### Generate SECRET_KEY
Run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## Step 5: Deploy

1. Click "Create Web Service"
2. Render will start building your project
3. Wait for deployment to complete (5-10 minutes)
4. You'll see a URL like: `https://haramaya-house-prediction.onrender.com`

---

## Step 6: Verify Deployment

1. Click the URL to visit your deployed app
2. You should see the homepage
3. Test the prediction feature
4. Check the about page

---

## Step 7: Troubleshooting

### If deployment fails:

1. **Check Build Logs**
   - Click "Logs" tab
   - Look for error messages
   - Common issues:
     - Missing dependencies in requirements.txt
     - Incorrect build command
     - Database migration errors

2. **Common Fixes**
   - Ensure all dependencies are in requirements.txt
   - Check SECRET_KEY is set
   - Verify ALLOWED_HOSTS includes your Render domain
   - Check database migrations run successfully

3. **View Live Logs**
   - Click "Logs" tab
   - See real-time application logs
   - Helps debug runtime errors

---

## Step 8: Update Your Project

### To deploy updates:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```
3. Render automatically redeploys on push (if auto-deploy is enabled)
4. Check deployment status in Render dashboard

---

## Step 9: Custom Domain (Optional)

1. In Render dashboard, go to your service
2. Click "Settings"
3. Scroll to "Custom Domain"
4. Enter your domain
5. Follow DNS configuration instructions

---

## Important Notes

### Free Plan Limitations
- Spins down after 15 minutes of inactivity
- Limited resources
- Good for testing/demo

### Production Recommendations
- Use **Starter** or higher plan
- Set up proper database (PostgreSQL)
- Use environment variables for sensitive data
- Enable auto-deploy from GitHub
- Set up monitoring and alerts

### Database
- Free plan uses SQLite (limited)
- For production, use PostgreSQL:
  1. Add PostgreSQL database in Render
  2. Update DATABASE_URL in environment
  3. Update settings.py to use PostgreSQL

---

## Useful Commands

### Generate Django Secret Key
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Test Locally Before Deploying
```bash
python manage.py runserver
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

---

## Your Deployed URLs

Once deployed, you can access:

- **Home**: `https://yourdomain.onrender.com/`
- **Predict**: `https://yourdomain.onrender.com/predict/`
- **Stats**: `https://yourdomain.onrender.com/predict/stats/`
- **About**: `https://yourdomain.onrender.com/about/`
- **Admin**: `https://yourdomain.onrender.com/admin/`
- **API**: `https://yourdomain.onrender.com/predict/api/predict/`

---

## Support

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com/
- GitHub Issues: Check your repository issues

---

**Your project is ready to deploy! Follow these steps and you'll be live in minutes.** 🚀
