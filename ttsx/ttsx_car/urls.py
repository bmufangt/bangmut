from django.conf.urls import url
import views

urlpatterns=[
    url(r'^car/$',views.car, name='car'),
]