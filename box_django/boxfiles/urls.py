from django.conf.urls import patterns, include, url

urlpatterns = patterns('boxfiles.views',
    url(r'^$', 'home', name='home'),
)
