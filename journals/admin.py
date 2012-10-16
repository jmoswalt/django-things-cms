from django.contrib import admin

from things.admin import ThingAdmin, ThingListFilter

from journals.forms import JournalForm
from journals.models import Journal


class AuthorListFilter(ThingListFilter):
    title = "Author"
    parameter_name = 'author'


class JournalAdmin(ThingAdmin):
    form = JournalForm
    list_display = ['name', 'link', 'content', 'author', 'temperature', 'journal_date']
    list_filter = [AuthorListFilter]
    ordering = ['-updated_at']

    def temperature(self, obj):
        if obj.temperature:
            return "%s &deg;F" % obj.temperature
        return ""
    temperature.allow_tags = True

admin.site.register(Journal, JournalAdmin)
