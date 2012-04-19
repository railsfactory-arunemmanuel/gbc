from django.conf.urls import patterns, include, url
from views import login,sample
from testapp.views import sampleform


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gbc.views.home', name='home'),
    # url(r'^gbc/', include('gbc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^login/',login),
    (r'^sample/',sample),
    (r'^sampleform/',sampleform),
)
