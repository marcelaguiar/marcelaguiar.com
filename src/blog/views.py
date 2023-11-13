from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home_view(request):
    return HttpResponse("blog root")