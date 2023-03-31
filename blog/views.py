from django.shortcuts import render,get_object_or_404

from django.utils import timezone
from .models import *

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/blog-home.html', context={'posts': posts})

def blog_single_view(request,pid):
    post = get_object_or_404(Post, pk=pid , published_date__lte=timezone.now())
    post.counted_views +=1
    post.save()
    next_post = Post.objects.filter(publish_status=True,
                                     published_date__gt=post.published_date,
                                        ).order_by('published_date').first()
    previous_post = Post.objects.filter(publish_status=True,
                                         published_date__lt=post.published_date,
                                            ).order_by('published_date').last()
    
    context = {'post': post, 'next_post': next_post, 'previous_post': previous_post}
    return render(request, 'blog/blog-single.html', context)