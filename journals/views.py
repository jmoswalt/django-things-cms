# views.py
from datetime import datetime

from django.views.generic import ListView, DetailView

from journals.models import Journal


class JournalDetailView(DetailView):
    model = Journal


class JournalListView(ListView):
    model = Journal

    def get_queryset(self, *args, **kwargs):
        super(JournalListView, self).get_queryset(*args, **kwargs)
        if self.request.user.is_superuser:
            queryset = Journal.objects.order_by('-published_at', '-created_at')
        else:
            queryset = Journal.objects.filter(
                published_at__gte=0,
                published_at__lte=datetime.now(),
                private=""
            )

            queryset = queryset.filter(datum__key="published_at").order_by('-datum__value')

        return queryset
