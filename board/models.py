from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64, default='default')
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=64, default='default')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )
    updated_at = models.DateTimeField(auto_now=True, editable=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.header
    def get_absolute_url(self):
        return reverse(
            'posts_list',
            #args=[str(self.id)]
        )

    def get_responses(self):
        return Response.objects.filter(pk=self.pk)

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='default',)
    submit = models.BooleanField(blank=True)





