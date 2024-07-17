from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_view(request: HttpRequest):

    return render(request, "home.html")

def about_view(request: HttpRequest):
    return render(request, "about.html")

def cities_view(request: HttpRequest):
   return render(request, "cities.html")

def agriculture_technologies_view(request: HttpRequest):
    return render(request, "agricultureTechnologies.html")



