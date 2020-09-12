from django.urls import path

from . import views
from .controllers.dashboard_view import DashboardView
from .controllers.dashboard_posts_view import DashboardPostsView

urlpatterns = [
    path('', views.index, name='index'),
    
    path('page/<slug:page_slug>', views.page_details, name='post_details'),
    path('category/<slug:category_slug>', views.category, name='category'),
    path('comment/<int:pk>', views.add_comment, name='comment'),

    # login and logout
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),

    # dashboard routes
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dashboard/posts', DashboardPostsView.as_view(), name='posts'),


    # post details like a wildcard
    path('<slug:post_slug>', views.post_details, name='post_details'),
    
]