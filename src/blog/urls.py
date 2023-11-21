from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home_view, name="blog_home"),
    path('post/<slug:slug>/', views.blog_home_view, name="blog_home"),
]
