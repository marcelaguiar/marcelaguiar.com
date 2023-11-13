from django.urls import path
from . import views

urlpatterns = [
    path('home', views.projects_home_view),
    path('', views.projects_home_view, name="projects_home"),
]
