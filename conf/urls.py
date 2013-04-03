from os.path import join

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'app_name.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': join(settings.PROJECT_ROOT, 'static')}
     ),
)


def get_app_url_patterns():
    items = []
    apps = settings.THINGS_APPS
    for app in apps:
        try:
            __import__('.'.join([app, 'urls']))
            items.append((r'', include('%s.urls' % app,)))
        except Exception as e:
            print "Skipping %s: %s" % (app, e)
            pass
    return patterns('', *items)

urlpatterns += get_app_url_patterns()
