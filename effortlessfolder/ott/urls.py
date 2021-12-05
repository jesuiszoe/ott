from django.contrib import admin
from django.urls import path
from . import views

# ott 관련 url
app_name = 'ott'
urlpatterns = [
    path('', views.main, name ='main'),
    path('amazon/', views.amazon, name='amazon'),
    path('hulu/', views.hulu, name='hulu'),
    path('disney/', views.disney, name='disney'),
    path('netflix/', views.netflix, name='netflix'),
    
    

    


]
