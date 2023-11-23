from rest_framework import routers

from src.apps.movie.views.movie import UserMovieRelationView, MovieViewSet

router = routers.SimpleRouter()
router.register('movie_relation', UserMovieRelationView)
router.register('',MovieViewSet)
urlpatterns = router.urls
