#!/use/bin/python
#-*-coding:utf-8-*-
"""SecNews URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import default,submit,search,sort,click
urlpatterns = [
	url(r'^$', default.index),
	url(r'^submit/$',submit.submit),
	url(r'^search/$',search.search),
    url(r'^admin/', include(admin.site.urls)),
    url(ur'^前端安全/(?P<taskid>\d+)/$', sort.sort),
    url(ur'^后端渗透/(?P<taskid>\d+)/$', sort.sort),
    url(ur'^漏洞分析/(?P<taskid>\d+)/$', sort.sort),
    url(ur'^夺旗竞赛/(?P<taskid>\d+)/$', sort.sort),
    url(ur'^神器分享/(?P<taskid>\d+)/$', sort.sort),
    url(ur'^程序之美/(?P<taskid>\d+)/$', sort.sort),
    url(r'^click/$',click.click),
]
