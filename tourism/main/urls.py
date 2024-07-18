from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('qatif/', views.qatif, name='qatif'),
    path('riyadh/', views.riyadh, name='riyadh'),
    path('holy/', views.holy, name='holy'),
    path('jeddah/', views.jeddah, name='jeddah'),
    path('ahsa/', views.ahsa, name='ahsa'),
    path('ula/', views.ula, name='ula'),
    path('food/', views.food, name='food'),
    path('light/', views.light, name='light'),
    path('dark/', views.dark, name='dark'),
]