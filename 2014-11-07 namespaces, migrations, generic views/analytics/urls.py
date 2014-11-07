from django.conf.urls import url, patterns
from django.views.generic import DetailView, ListView, TemplateView
from twitter.models import Tweet

urlpatterns = patterns('',
    url(
        r'^$',
        TemplateView.as_view(template_name="analytics/index.html"),
        name="index"
    ),
    url(
        r'^tweet/(?P<pk>\d+)',
        DetailView.as_view(model=Tweet)
    ),
    url(
        r'^tweets/',
        ListView.as_view(
            model=Tweet,
            paginate_by=3,
            template_name="analytics/tweet_list.html")
    )
)