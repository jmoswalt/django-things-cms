from django.contrib import admin

from things.admin import ThingAdmin

from .models import TemplateText
from .forms import TemplateTextForm


class TemplateTextAdmin(ThingAdmin):
    form = TemplateTextForm
    list_display = ['name', 'template_tag', 'content']


admin.site.register(TemplateText, TemplateTextAdmin)
