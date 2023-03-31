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

@register.inclusion_tag('blog/right-side/blog-popular-posts.html')
def popular_posts():
    posts = Post.objects.all().order_by('-counted_views')[:5]
    return {'pop_posts': posts}