# 🗄️ MySQL Database Setup Guide

## ✅ Changes Made

Your project now supports **both SQLite and MySQL**!

- **SQLite** - For local development (default)
- **MySQL** - For production deployment

---

## 📋 What Was Changed

### 1. **settings.py** - Updated database configuration
```python
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DB_NAME', default=str(BASE_DIR / 'db.sqlite3')),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}
```

### 2. **requirements.txt** - Added MySQL driver
```
mysqlclient==2.2.0
```

### 3. **.env.example** - Added MySQL environment variables

---

## 🚀 How to Use MySQL

### **Option 1: Local MySQL Setup**

#### Step 1: Install MySQL
**Windows:**
1. Download MySQL from: https://dev.mysql.com/downloads/installer/
2. Install MySQL Server
3. Remember your root password

**Mac:**
```bash
brew install mysql
brew services start mysql
```

**Linux:**
```bash
sudo apt-get install mysql-server
sudo systemctl start mysql
```

#### Step 2: Create Database
```sql
mysql -u root -p

CREATE DATABASE haramaya_house_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'haramaya_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON haramaya_house_db.* TO 'haramaya_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### Step 3: Create .env File
Create `.env` file in `haramaya_house_prediction/` folder:

```env
DEBUG=True
SECRET_KEY=django-insecure-haramaya-house-prediction-secret-key-2025
ALLOWED_HOSTS=localhost,127.0.0.1

# MySQL Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=haramaya_house_db
DB_USER=haramaya_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

#### Step 4: Install MySQL Client
```bash
pip install mysqlclient
```

**If you get errors on Windows:**
```bash
pip install pymysql
```

Then add to `config/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

#### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

#### Step 6: Run Server
```bash
python manage.py runserver
```

---

### **Option 2: Render with MySQL (Production)**

#### Step 1: Create MySQL Database on Render

1. Go to Render Dashboard: https://dashboard.render.com
2. Click **"New +"** → **"MySQL"**
3. Configure:
   - **Name:** `haramaya-mysql-db`
   - **Database:** `haramaya_house_db`
   - **User:** `haramaya_user`
   - **Region:** Same as your web service
   - **Plan:** Free or Starter
4. Click **"Create Database"**
5. Wait for database to be created
6. Copy the **Internal Database URL**

#### Step 2: Update Environment Variables in Render

Go to your Web Service → Settings → Environment Variables

Add these variables:

| Key | Value |
|-----|-------|
| `DB_ENGINE` | `django.db.backends.mysql` |
| `DB_NAME` | `haramaya_house_db` |
| `DB_USER` | (from Render MySQL dashboard) |
| `DB_PASSWORD` | (from Render MySQL dashboard) |
| `DB_HOST` | (from Render MySQL dashboard - Internal Host) |
| `DB_PORT` | `3306` |

#### Step 3: Redeploy

1. Go to **"Manual Deploy"** tab
2. Click **"Clear build cache & deploy"**
3. Wait for deployment to complete

---

### **Option 3: Use MySQL URL (Easier)**

If your MySQL provider gives you a URL like:
```
mysql://user:password@host:3306/database
```

Update `settings.py` to parse the URL:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}
```

Add to `requirements.txt`:
```
dj-database-url==2.1.0
```

Then set environment variable:
```
DATABASE_URL=mysql://user:password@host:3306/database
```

---

## 🔄 Switching Between SQLite and MySQL

### **Use SQLite (Local Development):**
In `.env`:
```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### **Use MySQL (Production):**
In `.env`:
```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=haramaya_house_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=3306
```

---

## 🐛 Troubleshooting

### **Error: "No module named 'MySQLdb'"**
**Solution:**
```bash
pip install mysqlclient
```

**On Windows, if that fails:**
```bash
pip install pymysql
```

Then add to `config/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### **Error: "Access denied for user"**
**Solution:**
- Check username and password
- Make sure user has privileges:
```sql
GRANT ALL PRIVILEGES ON haramaya_house_db.* TO 'haramaya_user'@'localhost';
FLUSH PRIVILEGES;
```

### **Error: "Can't connect to MySQL server"**
**Solution:**
- Check if MySQL is running:
```bash
# Windows
net start MySQL80

# Mac/Linux
sudo systemctl start mysql
```

- Check HOST and PORT are correct

### **Error: "Unknown database"**
**Solution:**
Create the database:
```sql
CREATE DATABASE haramaya_house_db;
```

---

## 📊 MySQL vs SQLite Comparison

| Feature | SQLite | MySQL |
|---------|--------|-------|
| **Setup** | Easy (no installation) | Requires MySQL server |
| **Performance** | Good for small apps | Better for large apps |
| **Concurrent Users** | Limited | Excellent |
| **Production Ready** | Not recommended | Yes |
| **Backup** | Copy file | mysqldump |
| **Scalability** | Limited | Excellent |

---

## ✅ Recommendations

### **For Local Development:**
- Use **SQLite** (easier, no setup needed)

### **For Production (Render):**
- Use **MySQL** or **PostgreSQL** (better performance, scalability)

### **For Small Projects:**
- SQLite is fine

### **For Large Projects:**
- Use MySQL or PostgreSQL

---

## 🎯 Current Configuration

Your project is now configured to:
- ✅ Use SQLite by default (local development)
- ✅ Support MySQL with environment variables
- ✅ Easy switching between databases
- ✅ Production-ready

---

## 📝 Next Steps

1. **For Local Development:**
   - Keep using SQLite (no changes needed)
   - Or install MySQL and follow "Option 1" above

2. **For Production (Render):**
   - Create MySQL database on Render
   - Add environment variables
   - Redeploy

---

**Your database is now flexible and production-ready!** 🚀
