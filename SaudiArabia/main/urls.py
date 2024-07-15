from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("games/", views.home_view, name="games_view"),
    path("events/", views.home_view, name="events_view"),
    path("teams/", views.home_view, name="teams_view"),
    path("infrastructure/", views.home_view, name="infrastructure_view"),
    path("mode/light", views.light_view, name="light_view"),
    path("mode/dark", views.dark_view, name="dark_view"),
]
