from things.views import ThingListView, ThingDetailView
from .models import Page


PUBLIC_FILTER_OUT = {'private': ""}


class PageDetailView(ThingDetailView):
    model = Page
    public_filter_out = PUBLIC_FILTER_OUT


class PageListView(ThingListView):
    model = Page
    public_filter_out = PUBLIC_FILTER_OUT
    super_user_order = ['-updated_at']
    public_order = "-updated_at"
