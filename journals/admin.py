from django.contrib import admin
from django.utils.text import truncate_words
from django.contrib.admin import SimpleListFilter

from things.admin import ThingAdmin

from journals.forms import JournalForm
from journals.models import Journal


class AuthorListFilter(SimpleListFilter):
    title = "Author"
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        result = []
        qs = Journal.objects.filter(datum__key='author').values('datum__value').order_by('datum__value').distinct()
        for q in qs:
            result.append((q['datum__value'], q['datum__value']))
        return tuple(result)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(datum__key='author').filter(datum__value=self.value())
        return queryset


class JournalAdmin(ThingAdmin):
    form = JournalForm
    list_display = ['name', 'link', 'content', 'author', 'temperature', 'journal_date']
    list_filter = [AuthorListFilter]
    ordering = ['-updated_at']

    def content(self, obj):
        return truncate_words(obj.content, 15)

    def temperature(self, obj):
        if obj.temperature:
            return "%s &deg;F" % obj.temperature
        return ""
    temperature.allow_tags = True

admin.site.register(Journal, JournalAdmin)
