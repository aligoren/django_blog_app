from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Post, Page, Setting
from .forms import CommentForm, LoginForm

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
    form = CommentForm()

    context = { 'post': post, 'settings': settings, 'form': form }

    return render(request, 'blog/details.html', context)

def page_details(request, page_slug):

    page = Page.objects.filter(slug=page_slug).first()
    settings = { 'title': page.title }

    context = { 'page': page, 'settings': settings }

    return render(request, 'blog/page_details.html', context)


def add_comment(request, pk):

    post = Post.objects.filter(pk=pk).first()
    settings = { 'title': post.title }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_details', post_slug=post.slug)
    else:
        form = CommentForm()

    context = { 'post': post, 'settings': settings, 'form': form }

    return render(request, 'blog/details.html', context)


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request, "Username or password not correct")
    else:
        form = LoginForm()

    settings = { 'title': 'Login' }
    context = { 'form': form, 'settings': settings }

    return render(request, 'auth/login.html', context)


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")


def handler404(request, exception):
    
    settings = { 'title': '404 Not Found' }

    context = { 'message': 'You may want to visit [Home](/)', 'details': str(exception), 'settings': settings  }
    
    return render(request, 'errors/404.html', context, status = 404)