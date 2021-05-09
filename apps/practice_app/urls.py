from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('view_data', views.view_data),
]