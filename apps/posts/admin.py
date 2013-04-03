from django.contrib import admin

from things.admin import ThingAdmin

from .forms import PostForm
from .models import Post


class PostAdmin(ThingAdmin):
    form = PostForm
    list_display = ['name', 'link', 'content', 'tags', 'published_at']


admin.site.register(Post, PostAdmin)
