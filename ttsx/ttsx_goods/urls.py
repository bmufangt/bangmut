from django.conf.urls import include, url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/([1-6])/', views.list, name='list'),
    url(r'^detail/(\d+)/', views.detail, name='detail'),
]