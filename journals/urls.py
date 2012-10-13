from django.conf.urls import patterns, url

from journals import views

urlpatterns = patterns('',
    url(r'^journals/$', views.JournalListView.as_view(), name='journal_list'),
    url(r'^journals/(?P<slug>[\w\-\/]+)/$', views.JournalDetailView.as_view(), name='journal_detail'),
)
