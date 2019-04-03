from django.conf.urls import patterns, include, url
from homepage.views import hello

urlpatterns = patterns('',
    url(r'^$', hello, name="homepage"),
    )