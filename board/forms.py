
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(forms.ModelForm):
    content = RichTextUploadingField()
    class Meta:
        model = Post
        fields = [
            'header',
            'category',
            #'author',
            'content',
        ]


class ResponseForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = [
            'text',
        ]