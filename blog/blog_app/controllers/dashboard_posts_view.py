from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Q

from ..models import Post, Setting
from ..forms import PostForm

class DashboardPostsView(LoginRequiredMixin, TemplateView):

    template_name = 'auth/posts.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    settings = { 'title': 'All Posts', 'dashboard': 'container-fluid' }

    def get(self, request):

        post_status = request.GET.get('status', 'published')
        page = request.GET.get('page', 1)
        search = request.GET.get('search', '')
        active = True

        if post_status == 'published':
            active = True
        elif post_status == 'draft':
            active = False
        elif post_status == 'all':
            active = None

        if search:
            post_list = Post.objects.filter(
                Q(active=active) & (Q(title__contains=search) | Q(content__contains=search))
            ).order_by('-id')
        else:
            post_list = Post.objects.filter(active=active).order_by('-id') if active is not None else Post.objects.all()
        
        settings = Setting.objects.first()

        

        paginator = Paginator(post_list, settings.posts_per_page)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
        context = { 'settings': self.settings, 'posts': posts }

        return render(request, self.template_name, context)