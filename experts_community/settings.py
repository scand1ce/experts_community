import os
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gcujteu5$u^&$1+g97omp_palol_3pp6^%t10ld57^icjxfgqt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #  --->
    'users.apps.UsersConfig',
    'my-admin.apps.AdminConfig',
    'storage.apps.StorageConfig',
    'posts.apps.PostsConfig',
    'chat',
    'commands',
    'channels',


    #  <--- 
    'crispy_forms',
    'django_extensions',




]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'experts_community.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'experts_community.wsgi.application'
ASGI_APPLICATION = 'chat.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'example',
        'HOST': 'localhost',
        'PORT': 5432,
        'CONN_MAX_AGE': 500
    }
}"""
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            "NAME": "d14l71t5dv496k",
            "USER": 'nrpqglhixflmvw',
            "PASSWORD": "b06a2e3d36737c51fee479073ecb049f9b745ab499dd96661dbea7e670dc969c",
            "HOST": "ec2-34-231-56-78.compute-1.amazonaws.com",
            "PORT": "5432",
            "URI": "postgres://nrpqglhixflmvw:b06a2e3d36737c51fee479073ecb049f9b745ab499dd96661dbea7e670dc969c@ec2-34-231-56-78.compute-1.amazonaws.com:5432/d14l71t5dv496k",
            "Heroku CLI": "heroku pg:psql postgresql-acute-67518 --app experts-community",
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'users/static'),

]

MEDIA_URL = '/media/'



AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.AllowAllUsersModelBackend',)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SHELL_PLUS = "ipython"

django_heroku.settings(locals())
