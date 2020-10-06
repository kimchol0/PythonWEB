from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^login/', views.login_view),
    url(r'^show/$', views.show_view)
]
