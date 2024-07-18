from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("games/", views.games_view, name="games_view"),
    path("events/", views.events_view, name="events_view"),
    path("teams/", views.teams_view, name="teams_view"),
    path("infrastructure/", views.infrastructure_view, name="infrastructure_view"),
    path("mode/light", views.light_view, name="light_view"),
    path("mode/dark", views.dark_view, name="dark_view"),
]
