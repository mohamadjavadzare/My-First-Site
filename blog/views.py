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
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)