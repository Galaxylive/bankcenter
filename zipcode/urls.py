from django.conf.urls import patterns, include, url
from zipcode import views

urlpatterns = patterns('',
    url(r'^$', views.PincodeView.as_view(), name='pincode_home'),
    url(r'^detail$', views.PincodeDetailView.as_view(), name='detail'),
    url(r'^city/(?P<city_slug>[\w-]+)/$', views.CityView.as_view(), name='city'),
    url(r'^(?P<pin>\d+)/$', views.PinDetailView.as_view(), name='pincode_pin_detail'),
)
