from django.test import TestCase
from tv.models import Channel

class testChannel(TestCase):

    def testCreateChannel(self):
        details = {'name':'CreateChannel','icon':'icon.create'};
        channel = Channel(**details)
        channel.save()

        self.assertIsInstance(channel, Channel)
        self.assertEqual(channel.name, details['name'])
        self.assertEqual(channel.icon, details['icon'])
