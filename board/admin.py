from django.contrib import admin
from django import forms
# Register your models here.
from ckeditor.widgets import CKEditorWidget

from .models import Post, Category, Response

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['header', 'author', 'category', 'created_at', 'updated_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Response, ResponseAdmin)