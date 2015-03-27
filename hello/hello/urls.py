from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
     url(r'^sh', include('shubham.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
