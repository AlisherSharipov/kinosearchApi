from rest_framework import serializers
from src.apps.movie.models.movie import Movie, UserMovieRelation


class MovieSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ('__all__')

    def get_likes_count(self, instance):
        return UserMovieRelation.objects.filter(movie=instance, like=True).count()




class UserMovieRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieRelation
        fields = ('movie', 'like', 'in_movie_favorites', 'rate')
