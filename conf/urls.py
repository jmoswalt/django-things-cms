from os.path import join

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_name.views.home', name='home'),
    url(r'^articles/', include('articles.urls')),
    url(r'^journals/', include('journals.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': join(settings.PROJECT_ROOT, 'static')}
    ),
)
