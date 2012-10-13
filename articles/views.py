# views.py
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(datum__key="published_at").order_by('-datum__value')
