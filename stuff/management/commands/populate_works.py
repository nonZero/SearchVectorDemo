import csv
import re
from pathlib import Path

import tqdm
from django.contrib.postgres.search import SearchVector
from django.core.management.base import BaseCommand
from django.db import transaction

from stuff.models import Row, Work


class Command(BaseCommand):
    help = "Populate works to DB"

    def handle(self, *args, **options):
        folder = Path('public_domain_dump/txt_stripped')
        # items = sorted(folder.glob("p*/m*.txt"))
        catalog = Path('public_domain_dump/pseudocatalogue.csv')
        with catalog.open() as f:
            docs = list(csv.DictReader(f))

        for d in tqdm.tqdm(docs):
            size = 0
            vid = int(d['ID'])
            p: Path = folder / f".{d['path']}.txt"
            size += p.stat().st_size
            work = Work.objects.get_or_create(
                vendor_id=vid,
                authors=d['authors'],
                title=d['title'],
            )[0]
            with transaction.atomic():
                work.rows.all().delete()
                with p.open() as f:
                    lines = f.read().splitlines()
                    rows = []
                    for i, line in enumerate(lines, 1):
                        line = line.strip()
                        if not line:
                            continue
                        rows.append(Row(
                            work=work,
                            ordinal=i,
                            content=line,
                        ))
                Row.objects.bulk_create(rows)
                # work.rows.update(sv=SearchVector('content'))

        print(f"{size:,d} bytes read.")
