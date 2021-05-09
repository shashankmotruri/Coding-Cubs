
from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.app_1.urls')),
    path('', include('apps.explore_app.urls')),
    path('', include('apps.practice_app.urls')),
    path('learn/', include('apps.learn_app.urls')),
    path('quiz/', include('apps.quiz_app.urls')),
]

urlpatterns += staticfiles_urlpatterns()