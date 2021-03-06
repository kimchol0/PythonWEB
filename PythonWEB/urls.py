"""PythonWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from PythonWEB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/', views.index_view),  # 正则表达式匹配路径hello，到views.py文件中的index_view函数
    url(r'^register/', include('stu.urls')),
    url(r'^student/', include('stu.urls')),
    url(r'^movie/', include('movie.urls'))
]
