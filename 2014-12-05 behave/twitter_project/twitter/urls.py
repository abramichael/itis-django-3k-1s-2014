
from django.conf.urls import url, patterns


urlpatterns = patterns('twitter.views',
    url(r'^$', 'home', name='home'),
    url(r'login/$', 'log_in', name='login'),
    url(r'logout/$', 'log_out', name='logout'),
    url(r'settings/$', 'settings', name='settings'),
    url(r'registration/$', 'registration', name='registration'),
)