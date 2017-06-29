from django.conf.urls import include, url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/([1-6])_(\d+)_([1-3])/', views.list, name='list'),
    url(r'^detail/(\d+)/', views.detail, name='detail'),
    url(r'^search', views.MySearchView()),
]