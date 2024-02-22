from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list),
    path('<slug:slug>/',views.article_detail), #P referes to the name given to the capture group.
]
