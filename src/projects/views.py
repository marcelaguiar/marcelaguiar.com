from django.shortcuts import render
from projects.models import Project


def projects_home_view(request):
    all_projects = Project.objects.all().order_by('-created')
    
    context = {
        'all_projects': all_projects
    }
    return render(request, 'projects/home.html', context)
