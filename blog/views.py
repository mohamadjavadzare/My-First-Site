from django.shortcuts import render,get_object_or_404

from django.utils import timezone
from .models import *

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    for post in posts: # turn publish_status on(Ture) if published_date is passed
        if post.publish_status == False:
            post.publish_status = True
            post.save()  

    if kwargs.get('cat_name') != None:  # posts by category
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    context={'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request,pid):
    post = get_object_or_404(Post, pk=pid , published_date__lte=timezone.now())
    post.counted_views +=1  # count views
    post.save()

    next_post = Post.objects.filter(publish_status=True,
                                     published_date__gt=post.published_date,
                                        ).order_by('published_date').first()
    previous_post = Post.objects.filter(publish_status=True,
                                         published_date__lt=post.published_date,
                                            ).order_by('published_date').last()
    
    context = {'post': post, 'next_post': next_post, 'previous_post': previous_post}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts =Post.objects.filter(published_date__lte=timezone.now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(summary__contains=s)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)