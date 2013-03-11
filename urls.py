from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import GenericSitemap
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from bank.models import Branch
branch_dict = {
    'queryset': Branch.objects.all(),
    'date_field': 'last_accessed' 
}

sitemaps = {
    'branches': GenericSitemap(branch_dict, priority=0.5)
}

urlpatterns = patterns('',
     url(r'^$', 'bank.views.home', name='home'),
     url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^atms/', include('atm.urls')),
     (r'^pincode/', include('zipcode.urls')),
     (r'^search/', include('haystack.urls')),
     (r'^bank/', include('bank.urls')),
)

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',  {'sitemaps': sitemaps}),
)
