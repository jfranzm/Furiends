from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Login and Sign UP page
    path('', views.index, name='login'),
    path('logged_In/', views.login_auth, name='login_page'),
    path('accounts/signup/', views.signup, name='signup'),

    # Main pages including Home, About
    path('home/<int:user_id>/', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Profile based templates and routes
    path('my_profile/', views.my_profile, name='my_profile'), 
    path('my_profile/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
    path('my_profile/<int:post_id>/', views.post_detail, name='post_detail'),

    # Post Create and Delete based routes views and templates
    path('post/create/<int:user_id>/', views.PostCreate, name='post_create'),
    path('post/create/<int:user_id>/post/', views.PostCreateComment, name='post_create_comment'),
    path('post/create/<int:user_id>/post/<int:post_id>/delete/', views.PostCreateDelete, name='post_create_delete'),

    # likes add and delete
    path('post/create/<int:user_id>/post/<int:post_id>/likes/', views.Likes_Create_Delete, name='like_create_delete'),
    path('post/create/<int:user_id>/post/<int:post_id>/total_likes/', views.total_likes, name='total_likes'),

]
