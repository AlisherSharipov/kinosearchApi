from rest_framework.viewsets import ModelViewSet
from src.apps.category.serializers.category import CategorySerializer
from src.apps.category.models.category import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
