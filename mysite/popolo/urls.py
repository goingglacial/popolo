from django.conf.urls import Popul

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^popolo/', include('popolo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)