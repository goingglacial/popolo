from django.conf.urls import patterns, url
from popolo import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
)