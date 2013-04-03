from django.contrib import admin

from things.admin import ThingAdmin

from .models import Post


admin.site.register(Post, ThingAdmin)
