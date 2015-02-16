from django.core.management.base import BaseCommand
from django.conf import settings

import datetime, os, xmltv

from operator import itemgetter
from collections import namedtuple
from tv.models import Channel

def _feed_exists():
    if os.path.isfile(settings.XML_TV_LISTING_FEED):
        return True
    else:
        return False

def _retrieve_channel_name(element):
    names = map(itemgetter(0), element['display-name'])
    return names[0]

def channels():
    channels = {}
    if _feed_exists():
        for key in xmltv.read_channels(open(settings.XML_TV_LISTING_FEED, 'r')):
            name = _retrieve_channel_name(key) 
            xml_id = key['id']
            src = key['icon'][0]['src']

            channel, _ = Channel.objects.get_or_create(name=name, xml_id=xml_id, icon=src)
            channels[channel.xml_id] = channel
    return channels

CHANNELS = channels()

def _retrieve_channel(id):
    return CHANNELS[id]


def _retrieve_title(element):
    titles = map(itemgetter(0), element['title'])
    return titles[0]

def _retrieve_description(element):
    if 'desc' in element:
        desc = map(itemgetter(0), element['desc'])
        return desc[0]
    return ''

def retrieve_information(element):
    return {
        'channel': _retrieve_channel(element['channel']),
        'description': _retrieve_description(element),
        'title': _retrieve_title(element),
        'start': format_time(element['start']),
        'stop': format_time(element['stop']),
    }

def format_time(timestamp):
    return datetime.datetime.strptime(timestamp[:12], "%Y%m%d%H%M%S")

class Command(BaseCommand):
    help = "Get the xml and whack it into the db"

    def handle(self, *args, **options):
        if _feed_exists():
            for element in xmltv.read_programmes(open(settings.XML_TV_LISTING_FEED, 'r')):
                information = retrieve_information(element)

        return 'Hi' 

