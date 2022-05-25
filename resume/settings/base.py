import os
from pathlib import Path

from decouple import config

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config("SECRET_KEY", get_random_secret_key())

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    # install
    "ordered_model",
    "tinymce",
    "sorl.thumbnail",
    # main
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "users.apps.UsersConfig",
    "about.apps.AboutConfig",
    "homepage.apps.HomepageConfig",
    "workshop.apps.WorkshopConfig",
]

MIDDLEWARE = [
    # main
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "resume.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.get_bootstrap_color"
            ],
        },
    },
]

WSGI_APPLICATION = "resume.wsgi.application"

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static_dev/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

LOGIN_URL = "/user/login"
LOGOUT_URL = "/user/logout"
LOGIN_REDIRECT_URL = "/user/"
