
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.blog_home_view),
    path('', views.blog_home_view),
]

