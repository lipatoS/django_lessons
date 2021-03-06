from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-osyy)yi$#n&p0!@#$%^&*(__st$*0p4d(+qtsj#@!&0d6vljh*@rv-r^z$q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
HTTP_SCHEMA = "http"
DOMEN = "localhost:8000"

INSTALLED_APPS = [
    # админская часть (база данных пользователя)
    'django.contrib.admin',
    # авторизация
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'currency',
    'accounts',
    'django_extensions',
    'debug_toolbar',
    'rangefilter',
    'import_export',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'currency.middlewares.ResponseTimeMW',
    'currency.middlewares.GclidMW',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# адрес компьютера
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
# порт 587
EMAIL_PORT = 587
EMAIL_HOST_USER = 'python.test.lipa@gmail.com'
EMAIL_HOST_PASSWORD = 'Python12578'
SUPPORT_EMAIL = 'python.test.lipa@gmail.com'
CELERY_BROKER_URL = 'amqp://localhost'

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "debug": {
        "task": "currency.tasks.parse_privarbank",
        "schedule": crontab(minute="*/1")
    },
    "1": {
        "task": "currency.tasks.parse_kurs_com_ua",
        "schedule": crontab(minute="*/1")
    },
    "2": {
        "task": "currency.tasks.parse_finance_i_ua",
        "schedule": crontab(minute="*/1")
    },
    "3": {
        "task": "currency.tasks.parse_minfin_com_ua",
        "schedule": crontab(minute="*/1")
    },
}
AUTH_USER_MODEL = "accounts.User"
from django.urls import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
