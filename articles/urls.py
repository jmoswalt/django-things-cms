from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns(
    '',
    url(r'^articles/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^articles/(?P<slug>[\w\-\/]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
)
