import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

# Load environment variables from the .env file
load_dotenv()

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Database
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DATABASE_ENGINE"),
        "NAME": BASE_DIR / os.getenv("DATABASE_NAME"),
    }
}

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=int(os.getenv("ACCESS_TOKEN_LIFETIME_DAYS"))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME_DAYS"))),
    'ROTATE_REFRESH_TOKENS': os.getenv("ROTATE_REFRESH_TOKENS") == "True",
    'BLACKLIST_AFTER_ROTATION': os.getenv("BLACKLIST_AFTER_ROTATION") == "True",
    'ALGORITHM': os.getenv("JWT_ALGORITHM"),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': (os.getenv("JWT_AUTH_HEADER_TYPE"),),
}

# Media
MEDIA_URL = os.getenv("MEDIA_URL")
MEDIA_ROOT = BASE_DIR / os.getenv("MEDIA_ROOT")

# Static
STATIC_URL = os.getenv("STATIC_URL")

# Internationalization
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE")
TIME_ZONE = os.getenv("TIME_ZONE")
USE_I18N = os.getenv("USE_I18N") == "True"
USE_TZ = os.getenv("USE_TZ") == "True"
