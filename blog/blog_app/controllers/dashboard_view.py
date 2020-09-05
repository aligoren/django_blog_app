from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages

from ..models import Post, Page, Comment
from ..forms import PostForm

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "auth/dashboard.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'Dashboard', 'dashboard': 'container-fluid' }

    def get(self, request):

        posts = Post.objects.all()
        pages = Page.objects.filter(active=True)
        comments = Comment.objects.filter(active=True)
        form = PostForm()

        details = { 
            'post_count': posts.count(), 
            'page_count': pages.count(),
            'comment_count': comments.count(),
            'last_posts': posts.order_by('-id')[:5],
            'last_comments': comments.order_by('-id')[:10]
        }

        context = { 'settings': self.settings, 'details': details, 'form': form }

        return render(request, self.template_name, context)
    
    def post(self, request):

        posts = Post.objects.all()
        pages = Page.objects.filter(active=True)
        comments = Comment.objects.filter(active=True)
        form = PostForm(request.POST, request.FILES)

        details = { 
            'post_count': posts.count(), 
            'page_count': pages.count(),
            'comment_count': comments.count(),
            'last_posts': posts.order_by('-id')[:5],
            'last_comments': comments.order_by('-id')[:10]
        }

        if form.is_valid():
            post = form.save()
            post.active = False
            post.save()
            messages.add_message(request, messages.INFO,'Post Added')
            return redirect('dashboard')
        else:
            form = PostForm()

        context = { 'settings': self.settings, 'details': details, 'form': form }

        return render(request, self.template_name, context)