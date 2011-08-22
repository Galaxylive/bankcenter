from django.conf.urls.defaults import patterns, include, url
from zipcode import views

urlpatterns = patterns('',
    url(r'^pincode$', views.pincode, name='pincode'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^pincode/city/(?P<city_id>[\w]+)/$', views.city, name='city'),                      
             
)
                          
