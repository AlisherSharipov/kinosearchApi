from django.contrib import admin
from ..movie.models.movie import Movie
from ..movie.models.actor import Actor

admin.site.register(Movie)
admin.site.register(Actor)