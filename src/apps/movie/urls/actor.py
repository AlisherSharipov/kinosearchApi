from rest_framework import routers
from src.apps.movie.views.actor import ActorViewSet

router = routers.SimpleRouter()
router.register('', ActorViewSet, basename='actor')
urlpatterns = router.urls
