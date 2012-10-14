from django import forms

from things.forms import ThingForm

from pages.models import Page


class PageForm(ThingForm):

    content = forms.CharField(widget=forms.Textarea, required=True)
    private = forms.BooleanField(required=False)
    priority = forms.IntegerField(required=False, initial=0)

    class Meta:
        model = Page
        exclude = ['obj_type']
