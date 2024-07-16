
from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse

def home_page(request):

  return render(request, "main/index.html")

def Aseer(request):
  return render(request, "main/Aseer.html")
def Sarawat(request):
  return render(request, "main/Sarawat.html")

def Marka(request):
   return render(request, "main/Marka.html")

def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))  
    response.set_cookie("mode", "dark", max_age=60*60*24*365)  
    return response

def light_mode(request):
    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.delete_cookie("mode")
    return response