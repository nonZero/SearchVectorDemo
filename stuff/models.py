from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Work(models.Model):
    vendor_id = models.PositiveIntegerField(unique=True)
    authors = models.CharField(max_length=500)
    title = models.CharField(max_length=500)


class Row(models.Model):
    work = models.ForeignKey(Work, related_name='rows', on_delete=models.CASCADE)
    ordinal = models.PositiveIntegerField()
    content = models.TextField()
    sv = SearchVectorField()

    class Meta:
        ordering = ('work', 'ordinal')
        unique_together = (
            ('work', 'ordinal'),
        )
        indexes = (
            GinIndex(fields=('sv',)),
        )
