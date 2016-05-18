"""arnel URL Configuration

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
from views import MyView, PlusTime

from book.views import AuthorCreateView, AuthorListView, AuthorDetailView, AuthorDeleteView, AuthorUpdateView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MyView.as_view()),
    url(r'^plus/$', PlusTime.as_view()),
    url(r'^plus/(?P<plus>[\d]+)/', PlusTime.as_view()),
    url(r'^author/create/$', AuthorCreateView.as_view()),
    url(r'^author/$', AuthorListView.as_view()),
    url(r'^author/(?P<pk>[\d]+)$', AuthorDetailView.as_view(), name='AuthorDetail'),
    url(r'^author/(?P<pk>[\d]+)/delete$', AuthorDeleteView.as_view()),
    url(r'^author/(?P<pk>[\d]+)/update$', AuthorUpdateView.as_view()),

]

