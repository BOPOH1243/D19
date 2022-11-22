from django.db.models import TextField
from django import forms
from board.models import Post, Response
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'header',
            'category',
            #'author',
            'content',
        ]