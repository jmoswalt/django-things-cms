from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from things.forms import ThingForm

from articles.models import Article


class ArticleForm(ThingForm):

    content = forms.CharField(widget=forms.Textarea, required=True)
    author = forms.CharField(required=False)
    publish_dt = forms.DateTimeField(required=True, widget=AdminSplitDateTime)
    featured = forms.BooleanField(required=False)

    class Meta:
        model = Article
        exclude = ['type']
