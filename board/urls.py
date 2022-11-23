from .views import *
from django.urls import path, include

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('createpost/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/editpost/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('responses/', ResponsesListView.as_view(), name ='responses_list'),
    path('responses/<int:pk>', ResponseDetailView.as_view(), name ='responses_list'),
    path('<int:pk>/createresponse/', CreatePostResponse.as_view(), name = 'create_post_response'),
    path('responses/<int:pk>/submit/', submit_response, name = 'submit_button')
]