from django.shortcuts import render
from django.http import HttpResponse

def projects_home_view(request):
    return HttpResponse("projects root")
