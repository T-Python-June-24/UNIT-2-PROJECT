from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path("", views.home_view, name="home_view"),
  path('city/<str:city_name>/', views.city_view, name="city_view"),
  path('destinations/', views.destination_view, name="destination_view"),
  path('about/', views.about_view, name="about_view"),
  path('guide/', views.guide_view, name="guide_view"),
]