"""
Django settings for DGADK project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vpdq+))%s2k5o33!e-bt9y_70lvdm(xly6=gbkkbe#fbte-^yd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'training',
    'automatic',
    'base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DGADK.urls'

WSGI_APPLICATION = 'DGADK.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DBS = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db3'),
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'172.16.0.200',
        'USER':'trb',
        'PASSWORD':'123',
        'NAME':'dgadk',
        'PORT':3306
    }
}
try:
    import sae
    DBS['saemysql'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':sae.const.MYSQL_HOST,
        'USER':sae.const.MYSQL_USER,
        'PASSWORD':sae.const.MYSQL_PASS,
        'NAME':sae.const.MYSQL_DB,
        'PORT':int(sae.const.MYSQL_PORT)
    }
    DATABASES = {
                 'default':DBS['saemysql']
                 }
    DEBUG = False
except:
    DATABASES = {
                 'default':DBS['mysql']
                 }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

FILE_CHARSET='utf-8'
DEFAULT_CHARSET='utf-8'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)




