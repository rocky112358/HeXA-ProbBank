from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^gameboard/', include('gameboard.urls', namespace='gameboard')),
    url(r'^notice/', include('noticeboard.urls', namespace='notice')),
]
