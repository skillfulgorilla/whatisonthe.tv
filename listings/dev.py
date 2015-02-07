from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'listings_dev',
        'USER': 'psqldev',
        'PASSWORD': '',
    }
}

DEBUG = True 
TEMPLATE_DEBUG = True
