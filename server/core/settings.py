"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⢘⢸⠀⡇⠁⠰⠀⡀⠆⢀⢰⠁⡇⡆⢸⢀⣁⣗⣺⢘⡀⡇⣱⠸⠀⠀⠆⠸⠐⠀⡇⣎⢸⠐⡃⣗⢸⣈⡂⡇⢰⢸⠀⡆⠂⢀⠰⠀⡄⠘⣿⣿⣿⣿⣿⣿
⠀⠀⠜⢸⠀⡇⠃⢠⠀⡄⡄⢸⢠⠀⡇⡄⢸⠤⠇⡧⢼⠸⠄⡇⢣⢰⠀⡀⡄⢸⢠⠀⡇⡼⢸⠤⠇⡧⢼⠸⠤⡇⢢⢰⠀⡅⡄⠈⢠⠀⡃⠸⣿⣿⣿⣿⣿⣿
⠀⠀⢱⢸⠀⡇⠀⢸⠀⣩⣇⢸⢨⡀⡏⡁⢸⠉⡆⣏⣹⢸⠁⡇⣎⢸⠀⠁⡁⠘⢈⠀⠃⣱⢸⣉⣇⣏⣽⣰⠁⡇⢈⢸⠀⠁⠀⠈⠈⠀⠃⢰⣿⣿⣿⣿⣿⣿
⠀⠀⢠⢰⠀⡁⡄⢈⠀⢻⣿⣷⣬⣤⠇⠣⢸⠐⡤⡇⢸⢰⠀⡇⡜⢈⠀⠀⠁⢠⠈⠀⡇⢣⢸⢐⣾⣿⣿⣦⠀⡇⠘⢘⠀⠅⠁⢠⠈⠀⡄⢠⣿⣿⣿⣿⣿⣿
⠀⠀⢈⢸⠀⡇⠁⠘⠀⡇⣿⡏⠙⢿⣷⣭⣹⢬⡉⡇⣼⣈⠄⡇⡱⢸⠀⡄⡇⢸⢸⡁⡇⣮⣽⣿⡿⠃⣿⣯⠄⡇⢹⢸⠀⠇⠂⠀⠰⠀⡀⢈⣿⣿⣿⣿⣿⣿
⠀⠀⠘⠘⠀⡇⠀⠸⠀⡄⣿⡇⠀⠀⠉⠿⣿⣷⣅⡇⢾⢘⣖⣇⣣⣸⣠⣄⣇⣸⣤⣤⣿⣿⠏⠉⢀⠀⢹⣿⠀⡇⢠⢸⠀⠀⠄⠀⢠⠀⠀⠘⣿⣿⣿⣿⣿⣿
⠀⠀⠸⢸⠀⡇⠇⢰⠀⠁⣻⣿⠀⠀⠀⠀⠈⠙⠻⣿⣿⠿⠛⠿⠛⠛⠛⠛⠛⠿⠿⠿⣿⡄⠀⠀⠀⠀⠘⣿⣇⡇⢍⢸⠠⡃⡤⢸⢀⠀⡃⠸⣿⣿⣿⣿⣿⣿
⠀⠀⢲⢸⠒⡇⠆⢨⠀⠃⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡚⢺⠐⡇⠅⠸⠘⠀⠇⢲⣿⣿⣿⣿⣿⣿
⠀⠀⢥⢸⠤⡇⡄⢸⢠⠆⢼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⡷⠾⢿⣬⡻⣿⣯⡤⡧⡇⢰⠼⠀⡦⢤⣿⣿⣿⣿⣿⣿
⠀⠀⣚⢸⡂⡇⡃⢸⠘⣆⡾⣿⡆⠀⠀⠀⠀⢀⣤⣾⠿⠿⠶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠈⠻⣿⣿⣿⣖⠏⢸⢰⠃⡇⢚⣿⣿⣿⣿⣿⣿
⠀⠀⠼⢸⠠⡇⠁⢸⠀⣤⣼⡿⡃⠀⠀⠀⠠⣾⠏⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⢐⠀⢿⣇⠀⠀⠀⠀⠀⠀⠈⢿⣞⣿⣧⢘⢠⠀⠁⠸⣿⣿⣿⣿⣿⣿
⠀⠀⣱⢸⠁⡇⣆⢸⣲⣿⡟⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⠀⠀⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⢿⣾⣿⣏⢈⠀⡇⢰⣿⣿⣿⣿⣿⣿
⠀⠀⢠⢸⠀⡇⠄⣸⣿⡟⠀⠀⠀⠀⠀⠁⠈⣿⠀⠀⠀⠀⠀⠀⡀⠀⠀⢹⡧⠀⠀⠀⠀⠀⠀⠺⣷⡄⠀⠀⢰⣾⣶⠀⢸⣿⢻⣿⡜⠀⡇⢠⣿⣿⣿⣿⣿⣿
⠰⢶⣭⣸⢈⡇⡈⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⡀⠀⠀⠀⣿⣿⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⢿⣦⡀⠀⠙⠁⢀⣸⡿⣆⣿⣿⣀⠆⣈⣿⣿⣿⣿⣿⣿
⠀⠀⠘⢹⠻⠶⣵⣿⠃⠀⠀⠀⠀⠀⠀⠀⢀⠈⠹⣷⣄⠀⠀⠈⠁⠀⣀⣼⠿⣂⡀⢠⣦⣦⣶⣶⣶⣶⡟⠛⠷⠦⢤⡾⠋⠀⠈⠙⠛⠿⣷⣾⣿⣿⣿⣿⣿⣿
⠀⠀⡹⢼⣀⡇⢸⣿⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣬⣽⠿⢶⣤⣤⣴⠿⠋⠀⠀⠉⠉⠻⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿
⢀⣀⣰⣸⣀⣇⣸⣿⣄⡀⠀⠀⠀⠀⠀⠀⢰⠞⠉⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣿⣿⣿⣿⣿⣿
⠈⠉⢉⢹⠛⡏⡽⣿⣿⠀⠀⠀⠀⠀⠄⠆⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠛⠶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⡚⢺⣒⡗⢓⠻⣿⣷⡀⠀⠀⠀⠂⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠉⠙⠛⠶⠶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿
⠀⠀⠼⢸⠀⡇⠧⢸⠙⣿⣿⣄⠀⠀⢀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⣛⣿⠟⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿
⠀⠀⣰⢸⠀⡇⡆⢸⡀⡉⠻⣿⣵⣄⡀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠘⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⣠⣿⡿⣿⣿⣿⣿⣿⣿
⠀⠀⢢⢸⠀⡇⠄⢈⠀⠇⠧⢨⠻⣿⣿⣢⢀⠀⠈⢑⢦⡀⠀⠀⠀⠀⠀⠉⠛⠶⣦⣤⣀⣀⣀⣤⣶⠾⠛⠉⠀⠀⠀⠀⠀⢀⣠⣶⣿⡿⡏⢦⣿⣿⣿⣿⣿⣿
⠀⠀⢈⢈⠀⠇⡀⠐⠀⡀⠇⢸⢰⣀⡟⠻⣿⣿⣶⣠⣄⢚⣷⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⢛⢹⡈⡇⠈⣿⣿⣿⣿⣿⣿
⠀⠀⠸⢸⠀⡇⠃⠠⠀⠀⡄⠈⢰⠂⡇⡔⢸⠉⠛⡿⢿⢿⣿⣿⣿⣭⣷⣶⣤⣄⣀⣀⣤⣤⣤⣤⣤⣴⣶⣾⡿⡿⢿⢻⠙⡆⡗⢺⢠⠀⠁⠘⣿⣿⣿⣿⣿⣿
⠀⠀⠹⢸⠀⡇⠁⢀⠀⠁⡁⠈⢈⠀⡏⡉⢸⠉⠇⣏⣹⢸⡀⡏⢏⠉⠉⠙⡛⢛⢛⠛⡉⡻⢹⢉⡍⣏⣸⠹⣉⡇⢈⢹⠈⠃⠁⠈⢈⠀⠃⠸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

from pathlib import Path
from os import environ
from dotenv import load_dotenv; load_dotenv()


getenv = environ.get

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('SECRET_KEY')

DEBUG = True if getenv('DEBUG').lower() == 'true' else False

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS').split(',')

PROJECT_APPS = [
    'inventory.apps.InventoryConfig'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

INSTALLED_APPS = PROJECT_APPS + DJANGO_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': f'django.db.backends.{getenv("DB_ENGINE")}',
            'HOST': getenv('DB_HOST'),
            'PORT': getenv('DB_PORT'),
            'NAME': getenv('DB_NAME'),
            'USER': getenv('DB_USER'),
            'PASSWORD': getenv('DB_PASSWORD'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
