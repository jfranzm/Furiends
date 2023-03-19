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
    path('post/create/<int:user_id>/photo/<int:photo_id>/', views.PostCreate, name='post_create'),
    path('post/create/<int:user_id>/post/photo/<int:photo_id>/', views.PostCreateComment, name='post_create_comment'),
    path('post/create/<int:user_id>/post/<int:post_id>/delete//photo/<int:photo_id>/', views.PostCreateDelete, name='post_create_delete'),

    # likes add and delete
    path('post/create/<int:user_id>/post/<int:post_id>/likes/photo/<int:photo_id>/', views.Likes_Create_Delete, name='like_create_delete'),
    path('post/create/<int:user_id>/post/<int:post_id>/total_likes/photo/<int:photo_id>/', views.total_likes, name='total_likes'),


    #  likes for PHOTO add and delete
    path('post/create/<int:user_id>/likes/photo/<int:photo_id>/', views.create_photo_like, name='photo_like'),
    path('post/create/<int:user_id>/likes/photo/<int:photo_id>/delete/', views.delete_photo, name='photo_delete')
]
