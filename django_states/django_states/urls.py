from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import GetPost
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),
    url(r'^get_post/', 'main.views.get_post'),
    url(r'^GetPost/', GetPost.as_view()),
)

