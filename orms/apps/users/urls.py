from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^new$',views.new),
    url(r'^create$',views.create),
    url(r'^show/(?P<id>\d+)$',views.show),
    url(r'^show/(?P<id>\d+)/destroy$',views.destroy),
    url(r'^show/(?P<id>\d+)/edit$',views.edit),
    url(r'^show/(?P<id>\d+)/update$',views.update),
]
