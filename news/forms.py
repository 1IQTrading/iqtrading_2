from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name','category','about', 'published','content',  'image', 'source')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'category', 'about', 'published', 'content', 'source')




