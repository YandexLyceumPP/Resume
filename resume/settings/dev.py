import os

from resume.settings import BASE_DIR, INSTALLED_APPS, MIDDLEWARE

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "dev-database.sqlite3"),
    },
}

STATIC_URL = "/static_dev/"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "emails"
