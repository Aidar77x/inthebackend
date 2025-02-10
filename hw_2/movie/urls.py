from django.urls import path
from .views import movie_list, movie_detail  # Убедись, что movie_detail теперь существует

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:id>/', movie_detail, name='movie_detail'),
]