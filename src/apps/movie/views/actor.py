from rest_framework.viewsets import ModelViewSet
from src.apps.movie.models.actor import Actor
from src.apps.movie.serializers.actor import ActorSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
