from django.core.management.base import BaseCommand
from django.conf import settings

import datetime, sys, xmltv

from operator import itemgetter
from collections import namedtuple

filename = settings.XML_TV_LISTING_FEED 
    
Channel = namedtuple('Channel', [
    'id', 'name', 'icon'
])

def channels():
    channels = {}
    try:
        for key in xmltv.read_channels(open(filename, 'r')):
            name = map(itemgetter(0), key['display-name'])
            id   = key['id']
            src  = key['icon'][0]['src']

            rec = dict(zip(Channel._fields, [id, name[0], src]))
            channel = Channel(**rec)
            channels[channel.id] = channel
    except IOError:
        print('There was an error opening the file!')
        sys.exit(0)

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
#        for element in xmltv.read_programmes(open(filename, 'r')):
#            information = retrieve_information(element)
        return 'Hi' 
