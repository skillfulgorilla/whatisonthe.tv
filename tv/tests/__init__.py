import os
from django.conf import settings

from testManagementCommands import testManagementCommand 
from testChannels import testChannel

settings.FIXTURE_DIRS = [os.path.join(os.path.dirname(__file__), "fixtures")]
settings.TESTING = True
