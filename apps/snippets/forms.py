from django import forms

from things.forms import ThingForm
from .models import Snippet


class SnippetForm(ThingForm):
    model = Snippet

    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)

        if 'allow_html' in self.fields:
            if self.instance.pk:
                if not self.fields['allow_html'].initial:
                    self.fields['content'].widget = forms.widgets.Textarea()
