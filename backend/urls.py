from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

urlpatterns = [
    path('', views.allLoc),
    path('ip/new/', views.addIp, name='addIp'),
    path('ip/create/', views.createIP, name='create-ip'),
    path('ip/del/<int:ip_id>/', views.deleteIp, name='deleteIp'),
]