from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tryDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('profiles.urls')),

)


# import xadmin
# xadmin. autodiscover ()

#  # Version module automatic registration required version control Model
# from xadmin.plugins import xversion
# xversion. registe_models ()

# urlpatterns = patterns ('',
#     url (r'xadmin / ', include (xadmin. site. urls)),
#  )
