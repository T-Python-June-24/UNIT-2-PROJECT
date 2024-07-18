from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html')


def games_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/games.html')


def events_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/events.html')


def teams_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/teams.html')


def infrastructure_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/infrastructure.html')


def dark_view(request: HttpRequest) -> HttpResponse:
    response = redirect("main:home_view")
    response.set_cookie("mode", "dark", max_age=86400)
    return response


def light_view(request: HttpRequest) -> HttpResponse:
    response = redirect("main:home_view")
    response.set_cookie("mode", "dark", max_age=-86400)
    return response
