from .base import *


DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CORS_ORIGIN_WHITELIST = [
    os.environ.get("CLIENT_URL"),
]