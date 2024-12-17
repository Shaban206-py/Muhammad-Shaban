from pathlib import Path
import os 
from decouple import config
from environ import Env
env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-1a8)(jd9^%ja0wjpqc(x*w1=culmyz%kkq-wej_x85bk)9es%4'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'main',  # your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # This tells Django to look inside the 'templates' folder
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# SECRET_KEY = 'django-insecure-1a8)(jd9^%ja0wjpqc(x*w1=culmyz%kkq-wej_x85bk)9es%4'
# DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True





# The path to the static files directory
# Static files configuration
STATIC_URL = '/static/'

# Add the 'static' directory from your app to STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),  # Path to the main/static directory
]

# The directory where static files will be collected during production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STORAGE = {
    "default":{
        "BACKEND":"django.core.files.storage.FilesSystemStorage",
    },
    "staticfiles":{
        "BACKEMD":"whitenoise.storage.CompressManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Use 'apikey' as the username for SendGrid
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY')  # Add your SendGrid API key to your .env file
