from django.urls import path, include

categories = [
    path('categories/',
         include(
             (
                 'src.apps.category.urls.category',
                 'src.apps.category'
             ),
             namespace='category'
         )
         ),
]
movie = [
    path('actors/',
         include(
             (
                 'src.apps.movie.urls.actor',
                 'src.apps.movie'
             ),
             namespace='actor'
         )
         ),
    path('movies/',
         include(
             (
                 'src.apps.movie.urls.movie',
                 'src.apps.movie'
             ),
             namespace='movie'
         )
         ),
]

urlpatterns = categories + movie
