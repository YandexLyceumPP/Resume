import os

from resume.settings import INSTALLED_APPS, BASE_DIR, MIDDLEWARE

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "dev-database.sqlite3"),
    },
}

DEBUG = True
