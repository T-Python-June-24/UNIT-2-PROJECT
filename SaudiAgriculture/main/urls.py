from django.urls import path
from . import views

app_main = "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("cities/", views.cities_view, name="cities_view"),
    path("agriculture-technologies/", views.agriculture_technologies_view, name="agriculture_technologies_view" ),
     path("dark/dark-mode/", views.dark_mode_view, name="dark_mode_view"),
    path("light/light-mode/", views.light_mode_view, name="light_mode_view"),
]
