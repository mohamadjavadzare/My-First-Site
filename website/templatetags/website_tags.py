from django import template
from blog.models import Post,Category
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.inclusion_tag('website/widgets/latest-posts.html', name='latest_posts')
def latest_posts(arg=6):
    posts = Post.objects.filter(publish_status= True).order_by('-published_date')[:arg]
    cat_dict = {}
    categories = Category.objects.all()
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'latest_posts': posts,'categories': cat_dict }


@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True