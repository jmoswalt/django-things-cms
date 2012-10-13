from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w\-\/]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
)
