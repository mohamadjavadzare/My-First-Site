from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=100)
    content = models.TextField()
    # category
    # tags
    counted_views = models.PositiveIntegerField(default=0)
    publish_status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
