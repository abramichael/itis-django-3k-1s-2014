
from django.conf.urls import url, patterns


urlpatterns = patterns('analytics.views',
    url(r'^$', 'home', name='home'),
)