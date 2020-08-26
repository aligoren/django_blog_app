from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Setting

def index(request):

    posts = Post.objects.all().order_by('-id')
    settings = Setting.objects.first()

    context = { 'posts': posts, 'settings': settings }

    return render(request, 'blog/index.html', context)

def post_defails(request, post_slug):

    post = Post.objects.filter(slug=post_slug).first()

    context = { 'post': post }

    return render(request, 'blog/details.html', context)