from django.shortcuts import render
from django.http import HttpResponse

def blog_home_view(request):
    return HttpResponse("blog root")
