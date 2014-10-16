from django.conf.urls import patterns, url
from popolo import views

urlpatterns = patterns('',
    url(r'^home$', views.home, name='home'),
    url(r'^search/(?P<prefix>[\w\ ]+)$', views.search, name='search'),
)