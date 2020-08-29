from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea is-fullwidth', 'rows': '5'}))

    class Meta:

        model = Comment

        fields = ('name', 'email', 'url', 'comment',)
        
