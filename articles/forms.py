from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from things.forms import ThingForm

from articles.models import Article


class ArticleForm(ThingForm):

    content = forms.CharField(widget=forms.Textarea, required=True)
    author = forms.CharField(required=False)
    published_at = forms.DateTimeField(required=False, widget=AdminSplitDateTime)
    featured = forms.BooleanField(required=False)

    class Meta:
        model = Article
        exclude = ['obj_type']
