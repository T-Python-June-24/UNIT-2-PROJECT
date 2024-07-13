from django.urls import path
from . import views

app_name = 'saudi_arabia'

urlpatterns = [
    path('', views.index, name='index'),
    path('dark_mode/', views.dark_mode, name='dark_mode'),
    path('light_mode/', views.light_mode, name='light_mode'),
    path('history/', views.history, name='history'),
]