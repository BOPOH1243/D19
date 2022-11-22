from .views import PostsListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView
from django.urls import path, include

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('createpost/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/editpost/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]