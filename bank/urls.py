from django.conf.urls import patterns, url

from bank import views


urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='bank_home'),
    url(r'^banks/$', views.BanksView.as_view(), name='bank_banks'),
    url(r'^cities/$', views.CitiesView.as_view(), name='bank_cities'),
    url(r'^ifsc/(?P<branch_ifsc>[A-Z0-9]+)/$', views.BranchIfscView.as_view(), name='bank_branch_with_ifsc'),
    url(r'^micr/(?P<branch_micr>[0-9]+)/$', views.BranchMicrView.as_view(), name='bank_branch_with_micr'),
    url(r'^city/(?P<location_slug>[a-zA-Z0-9_-]+)/$', views.CityBranchesView.as_view(), name='bank_city_branches'),
    url(r'^state/(?P<state_slug>[a-zA-Z0-9_-]+)/$', views.StateBranchesView.as_view(), name='bank_state_branches'),
    url(r'^state/(?P<state_slug>[a-zA-Z0-9_-]+)/(?P<bank_slug>[a-zA-Z0-9_-]+)/$', views.BankStateBranchesView.as_view(), name='bank_bank_state_branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/$', views.BankBranchesView.as_view(), name='bank_bank_branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<location_slug>[a-zA-Z0-9_-]+)/$', views.BankCityBranchesView.as_view(), name='bank_bank_city_branches'),
    # The regex below catches everything, come here in case of doubt.
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<branch_slug>[a-zA-Z0-9_-]+)/(?P<branch_ifsc>[A-Z0-9]+)/$', views.BranchInfoView.as_view(), name='bank_branch_info'),
)
