from django.contrib import admin

from things.admin import ThingAdmin, PrivateListFilter

from .forms import LinkForm
from .models import Link


class LinkAdmin(ThingAdmin):
    form = LinkForm
    list_filter = [PrivateListFilter]


admin.site.register(Link, LinkAdmin)
