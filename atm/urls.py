from django.conf.urls.defaults import patterns, include, url
from atm import views

urlpatterns = patterns('',
    url(r'^$', views.atms, name='atm_home'),
    url(r'^city/(?P<city_id>[\w-]+)/$', views.city, name='city'),                                         
    url(r'^bank/(?P<bank_id>[\w-]+)/$', views.bank, name='bank'),                                         
    url(r'^(?P<detail_id>[a-zA-Z0-9-/]+)/$', views.detail, name='detail'),                                                                
    #url(r'^detail$', views.detail, name='detail'),
    #url(r'^pincode/city/(?P<city_id>[\w]+)/$', views.city, name='city'),                      
)
                          

