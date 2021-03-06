from .base import *

DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '54.180.162.233']

CORS_ORIGIN_WHITELIST = [
    os.environ.get("CLIENT_URL"),
]

# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # strict mode 설정 추가
        }
    },
}

# STATIC

STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []