from django.conf.urls import patterns, include, url

from django.contrib import admin
from twitter.views import UserTweetListView, LoginView

admin.autodiscover()

urlpatterns = patterns('twitter.views',
    # Examples:
    url(r'^$', UserTweetListView.as_view(), name='index'),

    url(r'^page(?P<page>\d+)$', UserTweetListView.as_view(), name='index'),

    url(r'^proc/$', 'process', name='process'),
    url(r'^signin/$', LoginView.as_view(), name='sign_in'),

    url(r'^signout/$', 'sign_out', name='sign_out'),
    url(r'^q/$', 'q', name='q'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
)
