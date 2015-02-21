from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('dbname'),
        'USER': env('dbuser'),
        'PASSWORD': env('password'),
    }
}

DEBUG = False 
TEMPLATE_DEBUG = False 

SECRET_KEY = env('SECRET_KEY') 

XML_TV_LISTING_FEED = env('tv_listing_feed') 
