from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from .filters import PostFilter, ResponseFilter
from board.models import Post, Response

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'kabinet/index.html'

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'board/posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    #FIXME добавить пагинацию

    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class ResponsesView(LoginRequiredMixin, ListView):
    pass


class MyPostResponsesListView(LoginRequiredMixin, ListView):
    model = Response
    context_object_name = 'responses'
    template_name = 'kabinet/mypostresponses.html'

    def get_queryset(self):
        queryset = Response.objects.filter(post__author=self.request.user)
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context
