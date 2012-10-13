from os.path import join

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_name.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': join(settings.PROJECT_ROOT, 'static')}
    ),
)


def get_app_url_patterns():
    items = []
    apps = settings.INSTALLED_APPS
    for app in apps:
        if "things" not in app and "django" not in app:
            try:
                __import__('.'.join([app, 'urls']))
                items.append((r'', include('%s.urls' % app,)))
            except:
                pass

    return patterns('', *items)

urlpatterns += get_app_url_patterns()
