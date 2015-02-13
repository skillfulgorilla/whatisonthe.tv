from django.core.management import call_command
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.six import StringIO

class testManagementCommand(TestCase):

    def testCreateListings(self):
        out = StringIO()
        call_command('create_listings', stdout=out)
        self.assertIn('Hi', out.getvalue())

    @override_settings(XML_TV_LISTING_FEED = '/somewhere/else/')
    def testCreateListingsWithNoFile(self):
        out = StringIO()
        call_command('create_listings', stdout=out)
        print out.getvalue()
        self.assertIn('Hi', out.getvalue())
