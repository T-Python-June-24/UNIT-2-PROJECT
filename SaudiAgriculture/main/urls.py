from django.urls import path
from . import views

app_main = "main"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("cities/", views.cities_view, name="cities_view"),
]
