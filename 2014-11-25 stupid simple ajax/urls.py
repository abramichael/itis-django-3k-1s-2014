from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('twitter.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^proc/$', 'process', name='process'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^signout/$', 'sign_out', name='sign_out'),
    url(r'^q/$', 'q', name='q'),
    url(r'^get_users/$', 'get_users', name='get_users'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
)
