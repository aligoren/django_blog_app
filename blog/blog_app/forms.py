from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Comment

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