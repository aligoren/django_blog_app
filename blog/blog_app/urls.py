from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:post_slug>', views.post_defails, name='post_details')
]