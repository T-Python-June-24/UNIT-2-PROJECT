import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request: HttpRequest):
  with open('main/static/data/home_data.json', 'r') as file:
    home_data = json.load(file)
    
  context = home_data
  return render(request, "main/index.html", context)

def destination_view(request: HttpRequest):
   return render(request, "main/destination.html")

def about_view(request: HttpRequest):
   return render(request, "main/about.html")

def guide_view(request: HttpRequest):
   return render(request, "main/guide.html")

def city_view(request: HttpRequest, city_name: str):
    with open('main/static/data/city_data.json', 'r') as file:
      city_data = json.load(file)
    
    # Get the city data for the requested city
    context = city_data.get(city_name)
    return render(request, 'main/city_detail.html', context)
