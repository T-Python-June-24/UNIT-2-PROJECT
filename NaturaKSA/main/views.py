
from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse

from django.shortcuts import render

def home_page(request):
    cities = [
        {"title": "العلا", "url": "main:AlUla", "image": "/static/images/alula-landscape.jpg"},
        {"title": "الرياض", "url": "", "image": "/static/images/edge-of-the-world.jpg"},
        {"title": "الباحه", "url": "", "image": "/static/images/albaha.jpg"},
        {"title": "عسير", "url": "main:Aseer", "image": "/static/images/aseer.webp"},
        {"title": "جده", "url": "", "image": "/static/images/jeaddah-poster.jpg"},
        {"title": "الطائف", "url": "", "image": "/static/images/about-taif.webp"}
    ]
    return render(request, "main/index.html", {"cities": cities})

def Aseer(request):
  return render(request, "main/Aseer.html")
def Sarawat(request):
  return render(request, "main/Sarawat.html")

def Marka(request):
   return render(request, "main/Marka.html")
def AlUla(request):
   return render(request, "main/AlUla.html")
def flameـrace(request):
   return render(request, "main/flameـrace.html")
def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))  
    response.set_cookie("mode", "dark", max_age=60*60*24*365)  
    return response

def light_mode(request):
    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.delete_cookie("mode")
    return response


def city_base(request):
      return render(request, "main/city-base.html")
