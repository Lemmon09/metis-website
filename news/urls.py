from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('', 
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'aboutUs/$', views.aboutUs, name='aboutUs'),
    url(r'contactUs/$', views.contactUs, name='contactUs'),
    url(r'services/$', views.services, name='services'),

)