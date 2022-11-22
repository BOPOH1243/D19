from .views import PostsListView
from django.urls import path, include

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
]