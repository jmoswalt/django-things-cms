from django.conf.urls import patterns, url

from links import views

urlpatterns = patterns(
    '',
    url(r'^links/$', views.LinkListView.as_view(), name='link_list'),
    url(r'^links/(?P<slug>[\w\-\/]+)/$', views.LinkDetailView.as_view(), name='link_detail'),
)
