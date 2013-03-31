from things.views import ThingListView, ThingDetailView
from .models import Page


PUBLIC_FILTERS = {'private': ""}


class PageDetailView(ThingDetailView):
    model = Page
    public_filters = PUBLIC_FILTERS


class PageListView(ThingListView):
    model = Page
    public_filters = PUBLIC_FILTERS
    super_user_order = ['-updated_at']
    public_order = "-updated_at"
