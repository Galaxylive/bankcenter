from django.conf.urls.defaults import patterns, url

from bank import views


urlpatterns = patterns('',
    url(r'^$', views.home, name = 'bank_home'),
    url(r'^banks/$', views.banks, name = 'bank_banks'),
    url(r'^cities/$', views.cities, name = 'bank_cities'),
    url(r'^ifsc/(?P<branch_ifsc>[A-Z0-9]+)/$', views.branch_with_ifsc, name = 'bank_branch_with_ifsc'),
    url(r'^micr/(?P<branch_micr>[0-9]+)/$', views.branch_with_micr, name = 'bank_branch_with_micr'),
    url(r'^city/(?P<location_slug>[a-zA-Z0-9_-]+)/$', views.city_branches, name = 'bank_city_branches'),
    url(r'^state/(?P<state_slug>[a-zA-Z0-9_-]+)/$', views.state_branches, name = 'bank_state_branches'),
    url(r'^state/(?P<state_slug>[a-zA-Z0-9_-]+)/(?P<bank_slug>[a-zA-Z0-9_-]+)/$', views.bank_state_branches, name = 'bank_bank_state_branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/$', views.bank_branches, name = 'bank_bank_branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<location_slug>[a-zA-Z0-9_-]+)/$', views.bank_city_branches, name = 'bank_bank_city_branches'),
    # The regex below catches everything, come here in case of doubt.
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<branch_slug>[a-zA-Z0-9_-]+)/(?P<branch_ifsc>[A-Z0-9]+)/$', views.branch_info, name = 'bank_branch_info'),                       
)
