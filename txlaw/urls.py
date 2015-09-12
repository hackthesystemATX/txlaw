"""txlaw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from articles import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.landing),
    url(r'^search/$', views.search),
    url(r'^categories/(?P<num>[0-9]+)/$', views.category),
    url(r'^articles/(?P<num>[0-9]+)/$', views.article),
    url(r'^resources/(?P<num>[0-9]+)/$', views.resource),
#    url(r'^login/$', views.login),
#    url(r'^logout/$', views.logout),
#    url(r'^register/$', views.register),
]