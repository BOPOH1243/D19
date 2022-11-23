from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('myposts/', MyPostsView.as_view()),
    path('mypostresponses/', MyPostResponsesListView.as_view(), name='mypostresponses')
]