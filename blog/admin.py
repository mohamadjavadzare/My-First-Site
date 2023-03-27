from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Post)       # alterative way of registering
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'created_date', 'publish_status', 'published_date')
    list_filter = ('publish_status',)
    #ordering = ('-created_date',)
    search_fields = ['title', 'content']

admin.site.register(Post,PostAdmin)