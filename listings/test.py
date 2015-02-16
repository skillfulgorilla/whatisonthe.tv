from settings import *

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'sfp.sqlite3'}

INSTALLED_APPS += (
    'django_coverage',
) 

COVERAGE_REPORT_HTML_OUTPUT_DIR = 'cover'

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

XML_TV_LISTING_FEED = "tv/tests/fixtures/tv.xml"
