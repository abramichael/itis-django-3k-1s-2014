from django.conf.urls import patterns, include, url

from django.contrib import admin
from twitter_project import settings

admin.autodiscover()

urlpatterns = patterns('twitter.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^proc/$', 'process', name='process'),
    url(r'^signin/$', 'sign_in', name='sign_in'),
    url(r'^signout/$', 'sign_out', name='sign_out'),
    url(r'^q/$', 'q', name='q'),
    url(r'^edit/$', 'edit_avatar', name='edit_avatar'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),

)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }
    )
)
