from rest_framework import serializers
from src.apps.movie.models.movie import Movie, UserMovieRelation


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')


class UserMovieRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieRelation
        fields = ('movie', 'like', 'in_movie_favorites', 'rate')
