from django.shortcuts import render
from blog.models import Post


def blog_home_view(request):
    all_blog_posts = Post.objects.all().order_by('-created')
    
    context = {
        'all_blog_posts': all_blog_posts
    }
    return render(request, 'blog/home.html', context)
