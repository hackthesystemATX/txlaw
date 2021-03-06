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
    url(r'^$', views.landing, name='landing'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/(?P<id>[0-9]+)/$', views.search, name='search_category'),
    url(r'^categories/(?P<id>[0-9]+)/$', views.category, name='category'),
    url(r'^articles/(?P<id>[0-9]+)/$', views.article, name='article'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^resources/(?P<id>[0-9]+)/$', views.category_resources, name='category_resources'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
]
