from django.conf.urls import patterns, url
from popolo import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^results$', views.results, name='results'),
    url(r'^random$', views.random, name='random'),
    url(r'^fifty$', views.fifty, name='fifty'),
    url(r'^texas$', views.texas, name='texas'),
    # url(r'^state/_____$', views.texas, name='texas'),
)