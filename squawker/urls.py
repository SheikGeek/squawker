from django.conf.urls import patterns, include, url
from squawker import settings



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # squakwer/auth views
    url(r'^$', 'squawker.views.index'),
    url(r'^logout/$', 'squawker.views.logout'),
    url(r'^create_user/$', 'squawker.views.create_user'),

    # message views
    url(r'^m/create/$', 'messages.views.create_message'),
    url(r'^m/list/$', 'messages.views.list_messages'),

    # url(r'^squawker/', include('squawker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
