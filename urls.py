from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import GenericSitemap
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from bank.views import HomeView
from bank.models import Branch
branch_dict = {
    'queryset': Branch.objects.all(),
    'date_field': 'last_accessed'
}

sitemaps = {
    'branches': GenericSitemap(branch_dict, priority=0.5)
}


urlpatterns = patterns('',
   url(r'^$', HomeView.as_view(), name='home'),
   url(r'^robots\.txt$', TemplateView.as_view(
       template_name='robots.txt', content_type='text/plain')),
   # url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^atms/', include('atm.urls')),
   (r'^pincode/', include('zipcode.urls')),
   (r'^search/', include('haystack.urls')),
   (r'^bank/', include('bank.urls')),
)

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
)
