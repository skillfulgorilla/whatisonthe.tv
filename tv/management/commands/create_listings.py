from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Get the xml and whack it into the db"

    def handle(self, *args, **options):
        print "Hi"
