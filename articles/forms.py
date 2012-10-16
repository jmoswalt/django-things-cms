from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminSplitDateTime

from things.forms import ThingForm
from articles.models import Article

# CHOICES = [(u.get_full_name(), u.get_full_name()) for u in User.objects.all()]


class ArticleForm(ThingForm):
    model = Article

    # content = forms.CharField(widget=forms.Textarea, required=True)
    # author = forms.ChoiceField(required=False, widget=forms.Select, choices=CHOICES)
    # published_at = forms.DateTimeField(required=False, widget=AdminSplitDateTime)
    # featured = forms.BooleanField(required=False)
