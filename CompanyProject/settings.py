"""
Django settings for CompanyProject project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from google.oauth2 import service_account
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Is_Live = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7(@iyr&+5enzbmwyg+o6$&vhy@enhgp*w8n+bis1gt&l4^6=g#'
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!

if Is_Live == 1:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['35.200.244.164', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'support.apps.SupportConfig',
    'customers.apps.CustomersConfig',
    'project.apps.ProjectConfig',
    'announcement.apps.AnnouncementConfig',
    'blog.apps.BlogConfig',
    'website.apps.WebsiteConfig',
    'organization.apps.OrganizationConfig',
    'service.apps.ServiceConfig',
    'vendor.apps.VendorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CompanyProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CompanyProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if Is_Live == 1:

    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'companyproject',
            'USER': 'companyproject',
            'PASSWORD': 'Oyfsbho4sBGFngn9',
            # 'HOST': '127.0.0.1',
            'HOST': '/cloudsql/staticwebsite-274104:asia-northeast2:companyproject',
            'HOST': '34.97.28.181',
            'PORT': '3306'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'companyproject',
            'USER': 'root',
            'PASSWORD': '@Parvati!123',
            # 'HOST': '127.0.0.1',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(
        BASE_DIR, 'staticwebsite-274104-a13c760a65fd.json')
)

# Google Cloud Storage
if Is_Live == 1:
    GOOGLE_APPLICATION_CREDENTIALS = os.path.join(
        BASE_DIR, 'staticwebsite-274104-a13c760a65fd.json')

    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

    GS_ACCESS_KEY_ID = 'GOOG1EVPUZAMBWWHYZVOSVOQT5JAIFXFHRBK652MGE4TZKMMXIW7Y3LWUW5EQ'
    GS_SECRET_ACCESS_KEY = 'wiOwL/zcWpHAZ9HKSuYl5wvUdEIn+AXc3tVJWbe2'
    GS_BUCKET_NAME = 'prnson_bucket1'

    #xFlkwZMHKEzX33QzOu+774Ec5xD/ZpWfqT07wUMh

    # STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
else:
    GOOGLE_APPLICATION_CREDENTIALS = os.path.join(
        BASE_DIR, 'staticwebsite-274104-a13c760a65fd.json')
    
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_ACCESS_KEY_ID = 'GOOG1EVPUZAMBWWHYZVOSVOQT5JAIFXFHRBK652MGE4TZKMMXIW7Y3LWUW5EQ'
    GS_SECRET_ACCESS_KEY = 'wiOwL/zcWpHAZ9HKSuYl5wvUdEIn+AXc3tVJWbe2'
    GS_BUCKET_NAME = 'prnson_bucket1'

    # STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

if Is_Live == 1:
    STATICFILES_DIRS = [
        'https://storage.googleapis.com/prnson_bucket1/static/', ]
    STATIC_URL = 'https://storage.googleapis.com/prnson_bucket1/static/'
else:
    STATICFILES_DIRS = [BASE_DIR+'\\static']
    STATIC_URL = '/static/'

if Is_Live == 1:
    MEDIA_ROOT = 'https://storage.googleapis.com/prnson_bucket1/media/'
    MEDIA_URL = 'https://storage.googleapis.com/prnson_bucket1/media/'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = '/media/'
