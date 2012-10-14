from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from things.forms import ThingForm

from journals.models import Journal


class JournalForm(ThingForm):

    content = forms.CharField(widget=forms.Textarea, required=True)
    author = forms.CharField(required=False)
    journal_date = forms.DateTimeField(required=True, widget=AdminSplitDateTime)
    personal = forms.BooleanField(required=False)
    temperature = forms.FloatField(required=False)

    class Meta:
        model = Journal
        exclude = ['obj_type']
