import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv  # ✅ Load environment variables from .env file

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv("SECRET_KEY")  # ✅ Loaded from .env
DEBUG = os.getenv("DEBUG") == "True"  # ✅ Convert string to boolean
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")  # ✅ Convert to list

# Media settings
MEDIA_URL = os.getenv("MEDIA_URL")
MEDIA_ROOT = BASE_DIR / os.getenv("MEDIA_ROOT")

AUTH_USER_MODEL = "users.User"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'users',  # Custom apps
    'posts',
    'massagigng',
    'follow',
    'moderation',

    'rest_framework',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DATABASE_ENGINE"),
        "NAME": BASE_DIR / os.getenv("DATABASE_NAME"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE")
TIME_ZONE = os.getenv("TIME_ZONE")
USE_I18N = os.getenv("USE_I18N") == "True"
USE_TZ = os.getenv("USE_TZ") == "True"

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}
    
# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=int(os.getenv("ACCESS_TOKEN_LIFETIME_DAYS"))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME_DAYS"))),
    'ROTATE_REFRESH_TOKENS': os.getenv("ROTATE_REFRESH_TOKENS") == "True",
    'BLACKLIST_AFTER_ROTATION': os.getenv("BLACKLIST_AFTER_ROTATION") == "True",
    'ALGORITHM': os.getenv("JWT_ALGORITHM"),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': (os.getenv("JWT_AUTH_HEADER_TYPE"),),
}

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Enter: Bearer <JWT token>'
        }
    },
    'USE_SESSION_AUTH': False,
}

# Static files
STATIC_URL = os.getenv("STATIC_URL")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
