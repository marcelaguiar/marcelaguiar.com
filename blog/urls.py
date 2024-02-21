from django.urls import path
from blog.feeds import LatestEntriesFeed
from . import views

urlpatterns = [
    path('', views.blog_home, name="blog-home"),
    path('latest/feed/', LatestEntriesFeed(), name="rss-feed"),
    path('post/<int:id>/<slug:slug>/', views.blog_post, name="blog-post"),
]
