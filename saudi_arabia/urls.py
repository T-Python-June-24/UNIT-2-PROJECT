from django.urls import path
from . import views

app_name = 'saudi_arabia'

urlpatterns = [
    path('', views.index, name='index'),
    path('themes/dark_mode/', views.dark_mode, name='dark_mode'),
    path('themes/light_mode/', views.light_mode, name='light_mode'),
    path('history/', views.history, name='history'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('kings/', views.kings, name='kings'),
    path('future/', views.future, name='future'),
    path('save-selected-ingredients/', views.save_selected_ingredients, name='save_selected_ingredients'),
]