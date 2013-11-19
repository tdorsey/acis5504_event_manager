from django.conf.urls import patterns, url

from event_manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'event/(?P<event_id>\d+)/$', views.event, name='event'),
)
