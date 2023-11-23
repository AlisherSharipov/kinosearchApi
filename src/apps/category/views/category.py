from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from src.apps.category.serializers.category import CategorySerializer
from src.apps.category.models.category import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
