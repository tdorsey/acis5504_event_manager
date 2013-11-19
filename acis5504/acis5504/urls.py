from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event_manager/', include('event_manager.urls')),
    url(r'^$', include('event_manager.urls')),




)
