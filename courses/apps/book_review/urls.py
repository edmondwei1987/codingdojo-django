from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^regist$',views.regist),
    url(r'^login$',views.login),
    url(r'^add$',views.add),
    url(r'^process_add$',views.process_add),
    url(r'^book/(?P<id>\d+)$',views.book),
    url(r'^logout$',views.logout),
    url(r'^user/(?P<id>\d+)$',views.user),
]
