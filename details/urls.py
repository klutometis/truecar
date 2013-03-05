from django.conf.urls import patterns, url

from details import views

urlpatterns = \
    patterns('',
             url(r'^(?P<vehicle_id>\d+)/$', views.details, name='details'))
