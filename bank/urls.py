from django.conf.urls.defaults import patterns, include, url
from bank import views

urlpatterns = patterns('',
    url(r'^$',views.home,name='bank_home'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/$',views.bank_branches,name='bank_branches'),
    #url(r'^(?P<city_name>[a-zA-Z0-9_-]+)/$',views.city_branches,name='city branches'),
    url(r'^(?P<bank_slug>[a-zA-Z0-9_-]+)/(?P<branch_slug>[a-zA-Z0-9_-]+)/$',views.branch_info,name='bank_branch_info'),
)


