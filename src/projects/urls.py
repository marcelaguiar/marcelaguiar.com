from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_home_view, name="projects_home")
]
