from django.conf.urls import url
#from django.urls import re_path as url
from calc import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
