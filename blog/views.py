from django.shortcuts import render
from blog.models import Post


def blog_home(request):
    all_blog_posts = Post.objects.all().order_by('-created')
    
    context = {
        'all_blog_posts': all_blog_posts
    }
    return render(request, 'blog/home.html', context)

def blog_post(request, id, slug):
    blog_post = Post.objects.get(pk=id)
    
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/post.html', context)
