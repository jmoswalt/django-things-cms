# views.py
from django.views.generic import ListView, DetailView

from journals.models import Journal


class JournalDetailView(DetailView):
    model = Journal


class JournalListView(ListView):
    model = Journal
    queryset = Journal.objects.filter(datum__key="published_at").order_by('-datum__value')
