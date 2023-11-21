from django.shortcuts import render
from blog.models import Post


def blog_home_view(request):
    all_blog_posts = Post.objects.all().order_by('-created')
    
    context = {
        'all_blog_posts': all_blog_posts
    }
    return render(request, 'blog/home.html', context)

def blog_post(request, slug):
    blog_post = Post.objects.get(slug=slug)
    
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/post.html', context)
