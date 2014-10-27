from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^feed/', include('feed.urls', namespace="feed")),
    url(r'^login/$', login, {'template_name': 'project_1/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'project_1/logout.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
