from decouple import config

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "resume",
        "USER": config("DATABASE_USER", default="postgres"),
        "PASSWORD": config("DATABASE_PASSWORD", default="231860Aa"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("PORT", default="5432"),
    }
}

DEBUG = False

STATIC_URL = "/static/"
EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=True, cast=bool)
EMAIL_HOST = config("EMAIL_HOST", default="smtp.yandex.ru")
EMAIL_PORT = config("EMAIL_PORT", default=465, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
