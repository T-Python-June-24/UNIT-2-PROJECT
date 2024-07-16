from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path("", views.home_view, name="home_view"),
  path('city/<str:city_name>/', views.city_view, name="city_view"),
  path('history/', views.history_view, name="history_view"),
  path('events/', views.about_view, name="about_view"),
]