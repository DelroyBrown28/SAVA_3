from .base import *
import os

env = os.environ.copy()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'JvJhZBaDbVjqQSZOnUWfjRplI6XQtXs4GnfeOjN1qb4CDFQ4rFCVrBWkrbib'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*',  '127.0.0.1'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
