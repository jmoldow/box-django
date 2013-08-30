from django.conf.urls import patterns, include, url

urlpatterns = patterns('boxfiles.views',
    url(r'^$', 'home', name='home'),
    url(r'^fileview/(?P<file_id>\d+)$', 'fileview', name='fileview'),
)
