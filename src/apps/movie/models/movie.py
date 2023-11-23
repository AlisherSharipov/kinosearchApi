from django.db import models
from src.apps.movie.models.actor import Actor
from src.apps.common.models.base import CountryBase
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(CountryBase, on_delete=models.PROTECT, related_name='movies')
    date_release = models.DateField()
    actor = models.ManyToManyField(Actor, related_name='movies')
    description = models.TextField("Описание", blank=True)
    viewers = models.ManyToManyField(User, through='UserMovieRelation', related_name='movies')
    review = models.ForeignKey()

    def __str__(self):
        return self.title


class UserMovieRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_movie_favorites = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
