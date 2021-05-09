from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('view_info', views.view_info),
    url('read_article', views.read_article),
    url('favourites',views.favourites),
    url('feedback/',views.feedback),
]