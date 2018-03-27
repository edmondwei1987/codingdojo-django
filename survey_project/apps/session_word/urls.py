from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^addsession$', views.addsession),
    url(r'^clear$', views.clear),
]
