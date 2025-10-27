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
from django.urls import path

from goods import views
app_name = "goods"
urlpatterns = [
    path('index/', views.index),
    path('index2/', views.index2),
    path('index3/', views.index3),
    path('index5/', views.index5),
    path('index6/', views.index6),
    path('index7/', views.index7, name="index7"),
    path('index8/', views.index8),
    path('index9/', views.index9),
    path('index10/', views.index10),
    path('index11/', views.index11, name="index11"),  # name 设置路由别名
]
