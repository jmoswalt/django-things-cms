from datetime import datetime

from things.views import ThingDetailView, ThingListView
from .models import Post, PostPhoto


PUBLIC_FILTER_OUT = {'published_at__gte': 0,
                     'published_at__lte': datetime.now()}


class PostDetailView(ThingDetailView):
    model = Post
    public_filter_out = PUBLIC_FILTER_OUT


class PostListView(ThingListView):
    model = Post
    public_filter_out = PUBLIC_FILTER_OUT
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"


class PostPhotoDetailView(ThingDetailView):
    model = PostPhoto
