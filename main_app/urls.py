from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('logged_In/', views.login_auth, name='login_page'),
    path('home/<int:user_id>/', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('my_profile/', views.my_profile, name='my_profile'), 
    path('post/create/', views.PostCreate, name='post_create'),
    path('my_profile/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
    path('my_profile/<int:post_id>/', views.post_detail, name='post_detail')

]
