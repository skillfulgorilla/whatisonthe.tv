from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

# Create your tests here.

class ManagementCommandTests(TestCase):

    def testCreateListings(self):
        out = StringIO()
        call_command('create_listings', stdout=out)
        self.assertIn('Hi', out.getvalue())
