from django.urls import path
from . import views

urlpatterns = {
    path('create/', views.create_user),
    path('getall/', views.get_user_all),
    path(r'get/(?P<username>\w+)$', views.get_user_byusername),
}