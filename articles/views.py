from datetime import datetime

from things.views import ThingDetailView, ThingListView
from .models import Article


PUBLIC_FILTERS = {'published_at__gte': 0,
                  'published_at__lte': datetime.now()}


class ArticleDetailView(ThingDetailView):
    model = Article
    public_filters = PUBLIC_FILTERS


class ArticleListView(ThingListView):
    model = Article
    public_filters = PUBLIC_FILTERS
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"
