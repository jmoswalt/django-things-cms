from datetime import datetime

from things.views import ThingDetailView, ThingListView
from .models import Link


PUBLIC_FILTER_OUT = {'private': "",
                     'published_at__gte': 0,
                     'published_at__lte': datetime.now()}


class LinkDetailView(ThingDetailView):
    model = Link
    public_filter_out = PUBLIC_FILTER_OUT


class LinkListView(ThingListView):
    model = Link
    public_filter_out = PUBLIC_FILTER_OUT
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"
