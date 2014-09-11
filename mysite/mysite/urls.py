from django.conf.urls import patterns, include, url
from django.http import HttpResponse

from django.contrib import admin
admin.autodiscover()

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

urlpatterns = patterns('',
    url(r'^popolo', include('popolo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index)
)