from django.conf.urls import url
import views

urlpatterns=[
    url(r'^car/$',views.car, name='car'),
    url(r'^car_modify/$',views.modifycar_handle, name='modifycar_handle'),
    url(r'^car_del/$',views.delcar_handle, name='delcar_handle'),
]