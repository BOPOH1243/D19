from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from board.models import Post

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'kabinet/index.html'

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    #ordering = '-created_at'
    template_name = 'kabinet/myposts.html'
    context_object_name = 'posts'
    #FIXME добавить пагинацию
    '''def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user)
        return context'''

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
