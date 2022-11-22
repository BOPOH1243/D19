from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import *
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostsListView(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'board/posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    #FIXME добавить пагинацию из бутстрапа http://mybootstrap.ru/components/#pagination

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class PostCreateView(LoginRequiredMixin ,CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'board/post_edit.html'

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'board/post_edit.html'
    def form_valid(self, form):
        if self.get_object().author == self.request.user:
            return super().form_valid(form)
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['user'] = self.request.user
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        if self.get_object().author == self.request.user:
            return super().form_valid(form)
        else:
            return False

    def get_success_url(self):
        return super().get_success_url()