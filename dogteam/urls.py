from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dogteam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dogteam.views.landing', name='landing'),
    url(r'^test_page$', 'dogteam.views.test_page', name='test_page'),
    url(r'^recommend$', 'dogteam.views.recommend', name='recommend'),
    #url(r'^index$', 'dogteam.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
