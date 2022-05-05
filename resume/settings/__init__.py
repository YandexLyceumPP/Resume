from .base import *

DEBUG = config("DEBUG", default=True, cast=bool)

if DEBUG:
    from .dev import *
else:
    from .production import *
