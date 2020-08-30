from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:page_slug>', views.page_details, name='post_details'),
    path('category/<slug:category_slug>', views.category, name='category'),
    path('comment/<int:pk>', views.add_comment, name='comment'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('<slug:post_slug>', views.post_details, name='post_details'),
]