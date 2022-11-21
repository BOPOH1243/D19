from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, default='default')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=64, default='default')
    text = models.TextField(default='default', )
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )
    updated_at = models.DateTimeField(auto_now=True, editable=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #FIXME добавить картинки в текст

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





