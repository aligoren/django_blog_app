from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Page, Setting

def index(request):

    post_list = Post.objects.all().order_by('-id')
    settings = Setting.objects.first()

    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, settings.posts_per_page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = { 'posts': posts, 'settings': settings }

    return render(request, 'blog/index.html', context)

def category(request, category_slug):

    post_list = Post.objects.filter(category__slug=category_slug).order_by('-id')
    settings = Setting.objects.first()

    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, settings.posts_per_page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = { 'posts': posts, 'settings': settings }

    return render(request, 'blog/index.html', context)

def post_details(request, post_slug):

    post = Post.objects.filter(slug=post_slug).first()
    settings = { 'title': post.title }

    context = { 'post': post, 'settings': settings }

    return render(request, 'blog/details.html', context)

def page_details(request, page_slug):

    page = Page.objects.filter(slug=page_slug).first()
    settings = { 'title': page.title }

    context = { 'page': page, 'settings': settings }

    return render(request, 'blog/page_details.html', context)


def handler404(request, exception):
    
    settings = { 'title': '404 Not Found' }

    context = { 'message': 'You may want to visit [Home](/)', 'details': str(exception), 'settings': settings  }
    
    return render(request, 'errors/404.html', context, status = 404)