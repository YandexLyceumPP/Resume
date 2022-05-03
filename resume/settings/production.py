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
