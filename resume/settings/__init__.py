from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

if DEBUG:
    from .dev import *
else:
    from .dev import *
