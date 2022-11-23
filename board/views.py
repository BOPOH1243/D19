from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import *
from .filters import PostFilter, ResponseFilter
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

class ResponseCreateView(LoginRequiredMixin, CreateView):
    model = Response
    template_name = 'board/response_edit.html'
    success_url = reverse_lazy('posts_list')
    form_class = ResponseForm
    #FIXME дописать создание отклика


class ResponsesListView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'board/responses.html'
    context_object_name = 'responses'
    paginate_by = 3
    #FIXME добавить пагинацию из бутстрапа http://mybootstrap.ru/components/#pagination

    def get_queryset(self):
        queryset = Response.objects.filter(user=self.request.user)
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class CreatePostResponse(LoginRequiredMixin, CreateView):
    model = Response
    template_name = 'board/response_edit.html'
    success_url = reverse_lazy('posts_list')
    form_class = ResponseForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class ResponseDetailView(LoginRequiredMixin, DetailView):
    model = Response
    template_name = 'board/response.html'
    context_object_name = 'response'
    queryset = Response.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@login_required
def submit_response(request,pk):
    user = request.user
    response = Response.objects.get(pk=pk)
    if response.post.author == user:
        response.tosubmit()
        response.save()
    return redirect('/kabinet/mypostresponses/')