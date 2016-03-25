from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^scoreboard/$', views.scoreboard),
    url(r'^prob_view/(?P<prob_id>\d+)/$', views.prob_view),
    url(r'^auth/(?P<prob_id>\d+)/$', views.auth),
    url(r'^download/(?P<prob_id>\d+)/$', views.download),
]
