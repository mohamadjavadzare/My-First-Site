from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# @admin.register(Post)       # alterative way of registering
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'author', 'created_date', 'publish_status', 'published_date')
    list_filter = ('publish_status', 'author')
    #ordering = ('-created_date',)
    search_fields = ['title', 'content']
    summernote_fields = '__all__'
admin.site.register(Post,PostAdmin)

admin.site.register(Category)