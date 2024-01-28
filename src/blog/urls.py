from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name="blog-home"),
    path('post/<int:id>/<slug:slug>/', views.blog_post, name="blog-post"),
]
