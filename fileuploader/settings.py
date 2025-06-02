import os
from pathlib import Path
import dj_database_url
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Critical Koyeb fixes
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
CSRF_TRUSTED_ORIGINS = os.environ['CSRF_TRUSTED_ORIGINS'].split(',')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Disable Django's HTTPS redirect
USE_X_FORWARDED_HOST = True  # For Koyeb's proxy

# Keep your existing apps/middleware exactly as they were
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uploadapp',  # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database - PostgreSQL only
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files - only fix the typo
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Fixed spelling

# Media/Cloudinary - unchanged from your original
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

cloudinary.config(
    cloud_name=os.environ['CLOUDINARY_CLOUD_NAME'],
    api_key=os.environ['CLOUDINARY_API_KEY'],
    api_secret=os.environ['CLOUDINARY_API_SECRET'],
    secure=True
)

ROOT_URLCONF = 'fileuploader.urls'
WSGI_APPLICATION = 'fileuploader.wsgi.application'  # For production deployment

# Minimal production security
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True