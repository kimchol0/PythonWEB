from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view),  # 原生分页
    url(r'^index/$', views.index2_view)  # Django分页
]
