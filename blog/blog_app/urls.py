from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:post_slug>', views.post_details, name='post_details'),
    path('page/<slug:page_slug>', views.page_details, name='post_details'),
]