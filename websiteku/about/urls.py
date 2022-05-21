from django.conf.urls import url
from django.urls import URLPattern
from . import views
URLPattern =[
    url(r'$', views.index),
]