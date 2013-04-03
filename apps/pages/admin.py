from django.contrib import admin

from things.admin import ThingAdmin, PrivateListFilter

from .forms import PageForm
from .models import Page


class PageAdmin(ThingAdmin):
    form = PageForm
    list_filter = [PrivateListFilter]


admin.site.register(Page, PageAdmin)
