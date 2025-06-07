from .base import * 
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='django-insecure-m=!(*v54f%rj^^8irplhl#jrr!t#9mfqdgm%ahc2i_p68rg#2r'
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "192.168.1.137"]
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1"]
