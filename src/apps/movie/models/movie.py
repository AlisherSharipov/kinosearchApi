from django.db import models
from src.apps.movie.models.actor import Actor
from src.apps.common.models.base import CountryBase


class Movie(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(CountryBase, on_delete=models.PROTECT, related_name='movies')
    date_release = models.DateField()
    actor = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title
