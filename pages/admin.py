from django.contrib import admin

from things.admin import ThingAdmin, PrivateListFilter

from pages.forms import PageForm
from pages.models import Page


class PageAdmin(ThingAdmin):
    form = PageForm
    list_display = ['name', 'link', 'content', 'updated_at', 'private']
    list_filter = [PrivateListFilter]


admin.site.register(Page, PageAdmin)
