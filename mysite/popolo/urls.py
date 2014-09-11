from django.conf.urls import patterns, url
from popolo import views

urlspatterns = patterns('',
    url(r'^$', views.index, name='index')
)