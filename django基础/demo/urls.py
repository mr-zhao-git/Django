"""
URL configuration for django基础 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admindocs.views import TemplateDetailView
from django.urls import path,re_path

from django基础.dev import TEMPLATES
from .views import *
from django.views.generic import TemplateView




urlpatterns = [
    path('hello/', hello),
    re_path('^test1/$', test1),     #使用正则表达式进行添加路由
    re_path('^test2/([a-z]{3,8})/([0-9]{2})/$', test2),     #使用正则表达式进行添加路由
    re_path('^test3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', test3,name='zhao-test3'),     #使用正则表达式进行添加路由
    re_path('^test4/$', test4),
    re_path('^MyView/$', MyView.as_view()),     #路由地址是请求地址和视图函数的映射关系，所以不可以是MyView，而是MyView.as_view()
    re_path('^test6/$', test6),
    re_path('^test7/$', test7),
    re_path('^test8/$', test8),
    re_path('^test9/$', test9),
    re_path('^test10/$', test10),
    re_path('^index/$', TemplateView.as_view(template_name='index.html')),
    path("login",login),
    path("auth",auth),
]
