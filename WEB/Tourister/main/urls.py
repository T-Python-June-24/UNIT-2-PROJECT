from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('region/', views.region, name='region'),
    path('yanbu/', views.yanboa, name='yanbu'),
    path('festival/', views.festival, name='festival'),
    path('nawras_island/', views.nawras_island, name='nawras_island'),
]
