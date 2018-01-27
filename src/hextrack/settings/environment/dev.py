import os
from hextrack.settings import common

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bbcmy$(uqef#)2@#za47*p0aykca+@!+qj&fn5i=#-qjn=4#5q'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'hexuser',
        'PASSWORD': 'hexpassword',
        'NAME': 'hexdb',
        'HOST': 'localhost',
        'PORT': 5437
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
