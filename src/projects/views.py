from django.shortcuts import render


def projects_home_view(request):
    context = {}
    return render(request, 'projects/home.html', context)
