from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment, Post

class CommentForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea is-fullwidth', 'rows': '5'}))

    class Meta:

        model = Comment

        fields = ('name', 'email', 'url', 'comment',)
        

class LoginForm(AuthenticationForm):

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:

        model = User
        fields = ("username", "password")


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea is-fullwidth', 'placeholder': "What's on your mind?", 'rows': '5'}))
    cover_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input'}), required=False)

    class Meta:

        model = Post
        fields = ("title", "content", "cover_image")