from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dogteam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dogteam.views.landing', name='landing'),

    url(r'^admin/', include(admin.site.urls)),
)
