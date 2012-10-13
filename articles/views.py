# views.py
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article
