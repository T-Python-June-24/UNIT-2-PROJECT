from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('WhatToDo', views.WhatToDo, name='WhatToDo'),
    path('PlanYourTrip', views.PlanYourTrip, name='PlanYourTrip'),
    path('SaudiSeasons', views.SaudiSeasons, name='SaudiSeasons'),
    path('SaudiMap', views.SaudiMap, name='SaudiMap'),
    path('add_to_itinerary/', views.add_to_itinerary, name='add_to_itinerary'),

]
