from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_problem/$', views.add_problem),
    url(r'^add_notice/$', views.add_notice),
    url(r'^delete_problem/(?P<prob_id>\d+)/$', views.delete_problem),
    url(r'^edit_problem/(?P<prob_id>\d+)/$', views.edit_problem),
    url(r'^delete_notice/(?P<notice_id>\d+)/$', views.delete_notice),
    url(r'^edit_notice/(?P<notice_id>\d+)/$', views.edit_notice),
]
