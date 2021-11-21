from django.contrib import admin
from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    
    path('posts/', views.post_list, name='post-list'),
    path('posts/new', views.post_create, name='post-create'),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/<int:post_id>/edit', views.post_update, name='post-update'),
    path('posts/<int:post_id>/delete', views.post_delete, name='post-delete'),
    
    

    


]