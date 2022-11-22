from django.urls import path
from .views import IndexView, MyPostsView

urlpatterns = [
    path('', IndexView.as_view()),
    path('myposts/', MyPostsView.as_view())
]