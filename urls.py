from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     url(r'^admin/', include(admin.site.urls)),
     url(r'^atms/',include('atm.urls')),                      
     (r'^',include('zipcode.urls')),
     (r'^search/', include('haystack.urls')),
     (r'^',include('bank.urls')),
                       
     
)
urlpatterns += staticfiles_urlpatterns()
from bank_center.settings import DEBUG
from bank_center import settings
if DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
    ))
    
