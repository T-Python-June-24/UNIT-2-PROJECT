from django.urls import path
from . import views

app_name = 'Tourister'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_light/', views.home_light, name='home_light'),
    path('home_dark/', views.home_dark, name='home_dark'),
    path('kings/', views.kings, name='kings'),
    path('city/', views.city, name='city'),
    path('contact/', views.contact, name='contact'),
    path('card/', views.card, name='card'),
    path('chatbot/', views.agent, name='chatbot'),

]
