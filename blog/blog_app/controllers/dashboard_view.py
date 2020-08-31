from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ..models import Post, Page, Comment

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "auth/dashboard.html"
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'Dashboard', 'dashboard': 'container-fluid' }

    def get(self, request):

        posts = Post.objects.filter(active=True)
        pages = Page.objects.filter(active=True)
        comments = Comment.objects.filter(active=True)

        details = { 
            'post_count': posts.count(), 
            'page_count': pages.count(),
            'comment_count': comments.count(),
            'last_posts': posts.order_by('-id')[:5],
            'last_comments': comments.order_by('-id')[:10]
        }

        context = { 'settings': self.settings, 'details': details }

        return render(request, self.template_name, context)