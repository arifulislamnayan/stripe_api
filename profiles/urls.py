from django.conf.urls import patterns, include, url
from profiles import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tryDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),

    # url(r'^profiles/', include('profiles.urls')),

)