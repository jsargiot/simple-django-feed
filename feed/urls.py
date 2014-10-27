from django.conf.urls import patterns, url

from feed.views import home

urlpatterns = patterns(
    '',
    url(r'^$', home, name="home")
)
