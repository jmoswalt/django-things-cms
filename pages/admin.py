from django.contrib import admin
from django.utils.text import truncate_words

from things.admin import ThingAdmin

from pages.forms import PageForm
from pages.models import Page


class PageAdmin(ThingAdmin):
    form = PageForm
    list_display = ['name', 'link', 'content', 'updated_at', 'private']

    def content(self, obj):
        return truncate_words(obj.content, 15)

admin.site.register(Page, PageAdmin)
