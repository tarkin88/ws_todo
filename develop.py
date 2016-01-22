# from ws_todo import settings


SECRET_KEY = 'ete###n$m7#o)n1b^avy+u#pc$*78fjr*b^@ab^m(e4q29@p4g'

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGO_APPS = ''

THIRD_APPS = [
    'rest_framework'
]

INSTALLED_APPS = BASE_APPS + DJANGO_APPS + THIRD_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg1',
        'HOST': '',
        'NAME': 'ws_todo',
        'PORT': '',
        'USER': 'postgres',
        'PASSWORD': '',
    }
}
