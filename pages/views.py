# views.py
from django.views.generic import ListView, DetailView

from pages.models import Page


class PageDetailView(DetailView):
    model = Page


class PageListView(ListView):
    model = Page

    def get_queryset(self, *args, **kwargs):
        super(PageListView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_superuser:
            queryset = Page.objects.all().order_by('-updated_at')
        else:
            queryset = Page.objects.filter(private="").order_by('-updated_at')

        return queryset
