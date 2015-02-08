import os                                                                                                                      
from django.conf import settings

settings.FIXTURE_DIRS = [os.path.join(os.path.dirname(__file__), "fixtures")]
settings.TESTING = True
