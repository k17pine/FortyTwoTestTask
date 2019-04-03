from django.conf.urls import patterns,  url
from homepage.views import hello

urlpatterns = patterns('', url(r'^$', hello, name="homepage"))
