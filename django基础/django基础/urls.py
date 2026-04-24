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
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/',include('demo.urls')),  #如果前面不写表示所有的请求近来都去访问demo.urls
    path('demo1/',include('demo1.urls')),  #如果前面不写表示所有的请求近来都去访问demo.urls
    path('demo2/',include('demo2.urls')),  #如果前面不写表示所有的请求近来都去访问demo.urls
    path('django_orm/',include('django_orm.urls')),
    path('demo3/',include('demo3.urls')),
]
