from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Путь к этому файлу:
#   /Users/kirill 1/top-sklad-automation/backend/sklad/sklad/settings.py
# .parent => /Users/kirill 1/top-sklad-automation/backend/sklad/sklad
# .parent.parent => /Users/kirill 1/top-sklad-automation/backend/sklad
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^@d*_hh92_d!696j&^$(g@1@p5phl7*htp5*h-4ou$rs5rjfz6'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sklad',  # ваше приложение
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sklad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # папка с HTML-шаблонами
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

WSGI_APPLICATION = 'sklad.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sklad_db',
        'USER': 'sklad_user',
        'PASSWORD': 'sklad_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

AUTH_USER_MODEL = 'sklad.Users'

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

LANGUAGE_CODE = 'sk'
TIME_ZONE = 'Europe/Bratislava'
USE_I18N = True
USE_TZ = True

# Статика
STATIC_URL = '/static/'

# ВАЖНО: папка static у вас лежит в /Users/kirill 1/top-sklad-automation/backend/sklad/sklad/static
# BASE_DIR = /Users/kirill 1/top-sklad-automation/backend/sklad
# нужно добавить "sklad" ещё раз, чтобы получить /Users/kirill 1/top-sklad-automation/backend/sklad/sklad
STATICFILES_DIRS = [
    BASE_DIR / 'sklad' / 'static',
]

# Если в продакшене нужно собирать статику в одну папку:
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# Медиа (если используете ImageField/FileField)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'sklad' / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'moj_ucet'
