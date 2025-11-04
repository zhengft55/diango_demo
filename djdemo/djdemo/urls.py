"""
URL configuration for djdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path # 普通路由

from djdemo.op import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('goods/', include('goods.urls', namespace="goods")),
    path('mycookies/', include('mycookies.urls', namespace="mycookies")),
    path('sess/', include('sess.urls', namespace="sess")),
    path('rout/', include('re_rout.urls', namespace="rout")),
    path('cbv/', include('cbv.urls', namespace="cbv")),
    path('mymiddleware/', include('mymiddleware.urls', namespace="mymiddleware")),
    path('student/', include('student.urls', namespace="student")),
    path('redis/', include('redis_demo.urls', namespace="redis_demo")),

]
