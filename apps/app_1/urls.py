from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('home/',views.home , name='home'),
    path('explore/',views.explore_page, name='explore'),
    path('learn/',views.learn , name='learn'),
    path('practice/',views.practice_page , name='practice'),
]