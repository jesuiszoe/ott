from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ott'
urlpatterns = [
    path('', views.main, name ='main'),
    path('search', views.search, name='search'),
    

    


]
