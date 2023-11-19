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

urlpatterns = categories