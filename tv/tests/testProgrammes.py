from django.test import TestCase
from tv.models import Programme

class testProgramme(TestCase):

    def testCreateProgramme(self):
        details = {'title':'CreateProgramme'};
        programme = Programme(**details)
        programme.save()

        self.assertIsInstance(programme, Programme)
        self.assertEqual(programme.title, details['title'])
