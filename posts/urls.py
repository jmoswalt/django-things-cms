from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns(
    '',
    url(r'^posts/$', views.PostListView.as_view(), name='post_list'),
    url(r'^posts/(?P<slug>[\w\-\/]+)/$', views.PostDetailView.as_view(), name='post_detail'),
)
