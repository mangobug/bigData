from django.conf.urls import patterns, url

from bigData.main.views import traverse_data


urlpatterns = patterns('',

    url( r'^traverse/$',
        traverse_data,
        name = 'traverse_data' ),


)