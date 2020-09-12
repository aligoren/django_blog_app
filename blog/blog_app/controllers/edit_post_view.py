from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ..models import Post
from ..forms import PostForm

class EditPostView(LoginRequiredMixin, TemplateView):

    template_name = "auth/edit_post.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'Edit Post', 'dashboard': 'container-fluid' }

    def get(self, request, pk):

        posts = Post.objects.all()
        form = PostForm()

        details = { 
            'posts': posts, 
        }

        context = { 'settings': self.settings, 'details': details, 'form': form }

        return render(request, self.template_name, context)