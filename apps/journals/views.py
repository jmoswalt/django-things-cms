from datetime import datetime

from things.views import ThingDetailView, ThingListView
from .models import Journal


PUBLIC_FILTER_OUT = {'published_at__gte': 0,
                     'published_at__lte': datetime.now(),
                     'private': ""}


class JournalDetailView(ThingDetailView):
    model = Journal
    public_filter_out = PUBLIC_FILTER_OUT


class JournalListView(ThingListView):
    model = Journal
    public_filter_out = PUBLIC_FILTER_OUT
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"
