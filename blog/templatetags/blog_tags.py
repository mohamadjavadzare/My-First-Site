from django import template
from blog.models import *
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag(name='total_comments')
def get_total_comment():
    pass

@register.simple_tag(name='total_likes')
def get_total_like():
    pass

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.inclusion_tag('blog/right-side/blog-latest-posts.html', name='latest_posts')
def latest_posts(arg=5):
    posts = Post.objects.filter(publish_status= True).order_by('-published_date')[:arg]
    return {'pop_posts': posts}