from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #lets us append to the url pattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),#includes urls from articles app
    path('about/',views.about),
    path('',views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
