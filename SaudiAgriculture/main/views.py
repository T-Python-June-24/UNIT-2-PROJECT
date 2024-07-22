from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

def home_view(request: HttpRequest):

    return render(request, "home.html")

def about_view(request: HttpRequest):
    return render(request, "about.html")

def cities_view(request: HttpRequest):
   return render(request, "cities.html")

def agriculture_technologies_view(request: HttpRequest):
    return render(request, "agricultureTechnologies.html")

def dark_mode_view(request: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("dark", "dark-mode")
    return response


def light_mode_view(request: HttpRequest):

    response = redirect("home_view")
    response.set_cookie("light", "light-mode")
    return response




