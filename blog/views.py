from django.shortcuts import render
from blog.models import Post

from .forms import EmailForm


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

def email_subscribe(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    return render(request, "name.html", {"form": form})
