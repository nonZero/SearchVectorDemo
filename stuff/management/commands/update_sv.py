from django.contrib.postgres.search import SearchVector
from django.core.management.base import BaseCommand

from stuff.models import Work


class Command(BaseCommand):
    help = "Update SearchVectors"

    def handle(self, *args, **options):
        Work.objects.update(sv=SearchVector('content'))
