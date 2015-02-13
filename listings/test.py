from settings import *

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'sfp.sqlite3'}

INSTALLED_APPS += (
    'django_nose',
) 

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=tv',
    '--cover-html',
]

XML_TV_LISTING_FEED = "tv/tests/fixtures/tv.xml"
