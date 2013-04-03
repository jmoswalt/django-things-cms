from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^pages/$', views.PageListView.as_view(), name='page_list'),
    url(r'^(?P<slug>[\w\-\/]+)/$', views.PageDetailView.as_view(), name='page_detail'),
)
