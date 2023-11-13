from django.shortcuts import render


def blog_home_view(request):
    context = {}
    return render(request, 'blog/home.html', context)
