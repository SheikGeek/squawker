from django.conf.urls import patterns, include, url
from squawker import settings



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'squawker.views.index'),
    url(r'^logout/$', 'squawker.views.logout'),
    url(r'^create_user/$', 'squawker.views.create_user'),
    url(r'^mymedia/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    #url(r'^css/(?*.css)$', 'django.views.static.serve', {'document_root': '/css/'}),

    # url(r'^squawker/', include('squawker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
