
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^twitter/', include('twitter.urls',namespace='twitter')),
    url(r'^analytics/', include('analytics.urls',namespace='analytics')),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',
  		{'document_root' : settings.MEDIA_ROOT}
  		),

    url(r'^admin/', include(admin.site.urls)),
)
