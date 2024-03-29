from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #lets us append to the url pattern
from django.conf.urls.static import static 
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),#includes urls from articles app
    path('about/',views.about),
    path('',article_views.article_list,name="Home"),
    path('accounts/',include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
