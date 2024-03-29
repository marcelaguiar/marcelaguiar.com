from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from blog.models import Post, Subscriber


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
        email = request.POST["email"]
        new_subscriber = Subscriber(email=email, created_by_id=1, modified_by_id=1)
        save_result = True

        try:
            new_subscriber.save()
        except IntegrityError:
            print("User attempted to subscribe an email that is already subscribed: " + email)
        except:
            print("An unknown error occurred!")
            save_result = False
        
        return JsonResponse({'success': save_result})
