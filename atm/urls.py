from django.conf.urls import patterns, url

from atm import views

urlpatterns = patterns('',
   url(r'^$', views.AtmView.as_view(), name='atm_home'),
   url(r'^city/(?P<city_id>[\w-]+)/$',
       views.CityView.as_view(), name='atms_in_city'),
   url(r'^bank/(?P<bank_id>[\w-]+)/$',
       views.BankView.as_view(), name='atms_for_bank'),
   url(r'^(?P<city_id>[\w]+)/(?P<bank_id>[\w-]+)/(?P<detail_id>[0-9-/]+)/$',
       views.AtmDetailView.as_view(), name='atm_detail'),
)
