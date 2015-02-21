from django.test import TestCase
from tv.models import BroadCast, Channel, Programme

import datetime

class testBroadCasts(TestCase):

    def testBroadCastCreate(self):
        details = {'title': 'CreateProgramme'};
        programme = Programme(**details)
        programme.save()

        details = {'name':'CreateChannel','icon':'icon.create'};
        channel = Channel(**details)
        channel.save()
        
        now = datetime.datetime.today()
        details = {'channel': channel, 'start_time': now, 'end_time':now, 'programme': programme, 'blurb': 'this is a blurb'}
        broadcast = BroadCast(**details)
        broadcast.save()

        self.assertIsInstance(broadcast, BroadCast)
        self.assertEqual(broadcast.programme, details['programme'])
        self.assertEqual(broadcast.channel, details['channel'])
        self.assertEqual(broadcast.start_time, details['start_time'])
        self.assertEqual(broadcast.end_time, details['end_time'])
        self.assertEqual(broadcast.blurb, details['blurb'])


