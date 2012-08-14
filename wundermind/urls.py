from django.conf.urls import patterns, include, url
from words.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
)
