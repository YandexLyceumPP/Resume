from .base import *

DEBUG = False  # config("DEBUG", default=True, cast=bool)

if not DEBUG:
    from .dev import *
else:
    from .production import *
