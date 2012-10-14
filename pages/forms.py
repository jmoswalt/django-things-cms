from django import forms

from things.forms import ThingForm

from pages.models import Page


class PageForm(ThingForm):

    content = forms.CharField(widget=forms.Textarea, required=True)
    private = forms.BooleanField(required=False)

    class Meta:
        model = Page
        exclude = ['content_type_id']
