from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('home/',views.home , name='home'),
    path('explore/',views.explore, name='explore'),
    path('learn/',views.learn , name='learn'),
    path('practice/',views.practice , name='practice'),
    path('discuss/',views.discuss , name='discuss'),
]