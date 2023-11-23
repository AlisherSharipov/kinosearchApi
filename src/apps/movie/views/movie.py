from rest_framework import permissions
from rest_framework.mixins import UpdateModelMixin
from src.apps.movie.serializers.movie import UserMovieRelationSerializer, MovieSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from src.apps.movie.models.movie import UserMovieRelation, Movie


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class UserMovieRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserMovieRelation.objects.all()
    serializer_class = UserMovieRelationSerializer
    lookup_field = 'movie'

    def get_object(self):
        obj, _ = UserMovieRelation.objects.get_or_create(user=self.request.user, movie_id=self.kwargs['movie'])

        return obj
