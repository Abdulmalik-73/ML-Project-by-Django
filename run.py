#!/usr/bin/env python
"""
Simple script to run the Django development server
Usage: python run.py
"""
import os
import sys
import subprocess

def main():
    """Run the Django development server"""
    print("=" * 60)
    print("🚀 Starting Haramaya House Prediction Server")
    print("=" * 60)
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    # Check if manage.py exists
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Run migrations first
    print("\n📦 Running database migrations...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("✅ Migrations completed successfully!")
    except subprocess.CalledProcessError:
        print("⚠️  Warning: Migrations failed, but continuing...")
    
    # Collect static files
    print("\n📁 Collecting static files...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)
        print("✅ Static files collected!")
    except subprocess.CalledProcessError:
        print("⚠️  Warning: Static files collection failed, but continuing...")
    
    # Start the server
    print("\n" + "=" * 60)
    print("🌐 Starting Django development server...")
    print("=" * 60)
    print("\n📍 Server will be available at:")
    print("   🏠 Home:    http://127.0.0.1:8000/")
    print("   🔮 Predict: http://127.0.0.1:8000/predict/")
    print("   ℹ️  About:   http://127.0.0.1:8000/about/")
    print("   📊 Stats:   http://127.0.0.1:8000/predict/stats/")
    print("   👤 Admin:   http://127.0.0.1:8000/admin/")
    print("\n⏹️  Press CTRL+C to stop the server")
    print("=" * 60 + "\n")
    
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'])
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("🛑 Server stopped successfully!")
        print("=" * 60)
        sys.exit(0)

if __name__ == '__main__':
    main()
