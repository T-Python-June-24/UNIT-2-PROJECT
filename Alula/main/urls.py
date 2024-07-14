# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('experience/<int:pk>/', views.experience_detail, name='experience_detail'),
]
