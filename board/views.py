from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import *
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsListView(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'board/posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class PostCreate(LoginRequiredMixin ,CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)