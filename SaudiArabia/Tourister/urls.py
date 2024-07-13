# Tourister/urls.py
from django.urls import path
from . import views

app_name = 'Tourister'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_light/', views.home_light, name='home_light'),
    path('home_dark/', views.home_dark, name='home_dark'),
    path('kings/', views.kings, name='home_dark'),


]
