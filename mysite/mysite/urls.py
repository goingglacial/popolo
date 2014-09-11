from django.conf.urls import patterns, include, url
from django.contrib import admin
import popolo

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^popolo/', include(popolo.urls)),
    url(r'^admin/', include(admin.site.urls)),
)