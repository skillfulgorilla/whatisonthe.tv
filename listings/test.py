from settings import *
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = True

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'sfp.sqlite3'}

INSTALLED_APPS += (
    'django_coverage',
) 

COVERAGE_USE_CACHE = getattr(settings, 'COVERAGE_USE_CACHE', False)
COVERAGE_REPORT_HTML_OUTPUT_DIR = 'cover'
COVERAGE_USE_STDOUT = True 
COVERAGE_MODULE_EXCLUDES = getattr(settings, 'COVERAGE_MODULE_EXCLUDES', ['tests$', 'settings$', 'urls$', 'locale$', 'common.views.test', '__init__', 'django', 'migrations'])

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

XML_TV_LISTING_FEED = "tv/tests/fixtures/tv.xml"
