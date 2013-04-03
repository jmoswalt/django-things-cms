from django.contrib import admin

from things.admin import ThingAdmin, AuthorListFilter

from journals.forms import JournalForm
from journals.models import Journal


class JournalAdmin(ThingAdmin):
    form = JournalForm
    list_display = ['name', 'link', 'content', 'author', 'temperature', 'published_at']
    list_filter = [AuthorListFilter]
    ordering = ['-updated_at']

    def temperature(self, obj):
        if obj.temperature:
            return "%s &deg;F" % obj.temperature
        return ""
    temperature.allow_tags = True


admin.site.register(Journal, JournalAdmin)
