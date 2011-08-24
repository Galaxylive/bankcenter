from django.conf.urls.defaults import patterns, include, url
from atm import views

urlpatterns = patterns('',
    url(r'^atms$', views.atms, name='atm_home'),
    url(r'^atms/city/(?P<city_id>[\w-]+)/$', views.city, name='city'),                                         
    url(r'^atms/bank/(?P<bank_id>[\w-]+)/$', views.bank, name='bank'),                                         
    #url(r'^detail$', views.detail, name='detail'),
    #url(r'^pincode/city/(?P<city_id>[\w]+)/$', views.city, name='city'),                      
)
                          
