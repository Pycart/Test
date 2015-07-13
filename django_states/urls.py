from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from main.views import GetPost

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_states.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # (?P<starts_with>\w+)

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^get_post_but_why/$', 'main.views.get_post_but_why'),
    url(r'^get_post/$', 'main.views.get_post'),
    url(r'^GetPost/$', csrf_exempt(GetPost.as_view())),

)
