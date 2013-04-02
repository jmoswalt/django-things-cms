from datetime import datetime

from things.views import ThingDetailView, ThingListView
from .models import Article


PUBLIC_FILTER_OUT = {'published_at__gte': 0,
                     'published_at__lte': datetime.now()}


class ArticleDetailView(ThingDetailView):
    model = Article
    public_filter_out = PUBLIC_FILTER_OUT


class ArticleListView(ThingListView):
    model = Article
    public_filter_out = PUBLIC_FILTER_OUT
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"
