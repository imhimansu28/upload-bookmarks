import environ

from .base import *  # noqa

env = environ.Env()

# reading .env file
environ.Env.read_env()

DEBUG = True
ALLOWED_HOSTS = [
    "127.0.0.1",
]
INTERNAL_IPS = ["127.0.0.1"]
SITE_URL = "127.0.0.1:8080"

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Set DJANGO_DISABLE_LOCAL_CACHE in environment variables
# to disable cache during development
CACHE_BACKEND = "django.core.cache.backends.locmem.LocMemCache"
CACHES = {
    "default": {
        "BACKEND": CACHE_BACKEND,
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# TOOLBAR CONFIGURATION
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE  # noqa

# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_USE_TLS = env("EMAIL_USE_TLS")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
