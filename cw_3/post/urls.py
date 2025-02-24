from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),  # Список Thread
    path('<int:id>/', views.thread_detail, name='thread_detail'),  # Детали Thread + Posts
    path('<int:id>/delete/', views.thread_delete, name='thread_delete'),  # Удаление Thread
    path('<int:id>/edit/', views.thread_edit, name='thread_edit'),  # Редактирование Thread
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),  # Удаление Post
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),  # Редактирование Post
]
