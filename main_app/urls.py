from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pictures/<int:picture_id>/add_photo/', views.add_photo, name='add_photo')
]
