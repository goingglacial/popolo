from django.conf.urls import patterns, url
from popolo import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^bubbles$', views.bubbles, name='bubbles'),
    url(r'^results$', views.results, name='results'),
    url(r'^random$', views.random, name='random'),
    url(r'^fifty$', views.fifty, name='fifty'),
    url(r'^texas$', views.texas, name='texas'),
    url(r'^about$', views.about, name='about'),
    url(r'^states/(?P<statename>\w+)$', views.states, name='states'),
    url(r'^search/(?P<prefix>[\w\ ]+)$', views.search, name='search'),
)