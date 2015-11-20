from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from bigData.main.views import index

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url( r'^$', index, { 'template_name': 'main/index.html' }, name = 'index' ),

    url(r'^main/', include('bigData.main.urls')),
)
