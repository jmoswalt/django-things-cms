from django.conf.urls import patterns, url

from journals import views

urlpatterns = patterns('',
    url(r'^$', views.JournalListView.as_view(), name='journal_list'),
    url(r'^(?P<slug>[\w\-\/]+)/$', views.JournalDetailView.as_view(), name='journal_detail'),
)
