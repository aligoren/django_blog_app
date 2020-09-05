from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ..models import Post, Setting
from ..forms import PostForm

class DashboardPostsView(LoginRequiredMixin, TemplateView):

    template_name = 'auth/posts.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'All Posts', 'dashboard': 'container-fluid' }

    def get(self, request):

        post_list = Post.objects.filter(active=True).order_by('-id')
        settings = Setting.objects.first()

        page = request.GET.get('page', 1)

        paginator = Paginator(post_list, settings.posts_per_page)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context = { 'settings': self.settings, 'posts': posts }

        return render(request, self.template_name, context)