from django.contrib.postgres.search import SearchVector
from django.core.management.base import BaseCommand

from stuff.models import Row


class Command(BaseCommand):
    help = "Update SearchVectors"

    def handle(self, *args, **options):
        Row.objects.update(sv=SearchVector('content'))
