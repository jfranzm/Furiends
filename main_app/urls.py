from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('pictures/<int:picture_id>/add_photo/', views.add_photo, name='add_photo')
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
]
