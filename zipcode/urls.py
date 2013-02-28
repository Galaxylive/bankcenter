from django.conf.urls.defaults import patterns, include, url
from zipcode import views

urlpatterns = patterns('',
    url(r'^$', views.pincode, name='pincode_home'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^city/(?P<city_slug>[\w-]+)/$', views.city, name='city'),                      
    url(r'^(?P<pin>\d+)/$', views.pin_detail, name='pincode_pin_detail'),
)
