from django.conf.urls.defaults import patterns, include, url
from bank import views

urlpatterns = patterns('',
    url(r'^$',views.home,name='bank_home'),
    url(r'cities/$',views.cities,name='bank_cities'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/$',views.bank_branches,name='bank_bank_branches'),
    url(r'^banks/city/(?P<location_slug>[a-zA-Z0-9_-]+)/$',views.city_branches,name='bank_city_branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<branch_slug>[a-zA-Z0-9_-]+)/$',views.branch_info,name='bank_branch_info'),
    url(r'^banks/state/(?P<state_slug>[a-zA-Z0-9_-]+)/$',views.state_branches,name='bank_state_branches'),    
)


