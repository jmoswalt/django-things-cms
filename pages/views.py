# views.py
from django.views.generic import ListView, DetailView

from pages.models import Page


class PageDetailView(DetailView):
    model = Page


class PageListView(ListView):
    model = Page
    queryset = Page.objects.all().order_by('-updated_at')
