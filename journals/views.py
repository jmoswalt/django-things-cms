# views.py
from django.views.generic import ListView, DetailView

from journals.models import Journal


class JournalDetailView(DetailView):
    model = Journal


class JournalListView(ListView):
    model = Journal

    def get_queryset(self, *args, **kwargs):
        super(JournalListView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_superuser:
            queryset = Journal.objects.all()
        else:
            queryset = Journal.objects.filter(personal="")

        queryset = queryset.filter(datum__key="journal_date").order_by('-datum__value', '-created_at')

        return queryset
