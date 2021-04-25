from .base import *

DEBUG = True

SECRET_KEY = '_r9qyv0km^8i@v#jnvj)1t3409$sit8ty74(y29-1&!w+70b82'

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}