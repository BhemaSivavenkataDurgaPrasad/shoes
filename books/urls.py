 

from django.contrib import admin
from django.urls import path
from .views import Home_page,Shop_page
from . import views 

urlpatterns = [
    
    path('', views.Home_page ,name = 'Home'),
    path('Shop_page/', views.Shop_page, name = 'Shop_page'), 
    path('collection_page/', views.collection_page, name = 'collection_page'), 
    path('racing/' , views.racing_page,name = 'racing'),
    path('contact/' ,views.contact_page,name = 'contact'),


]
