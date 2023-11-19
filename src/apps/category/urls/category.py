from rest_framework import routers
from src.apps.category.views.category import CategoryViewSet

router = routers.SimpleRouter()
router.register('', CategoryViewSet, basename='category')
urlpatterns = router.urls
