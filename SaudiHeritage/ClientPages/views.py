from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.


def index(request:HttpRequest):
    return render(request , 'pages/index.html')

def Regions(request:HttpRequest):
    return render(request , 'pages/Regions.html')

def RjalAlma(request:HttpRequest):
    return render(request , 'pages/rjal_alma.html')
def alanga(request:HttpRequest):
    return render(request , 'pages/alanga.html')

def mard(request:HttpRequest):
    return render(request , 'pages/mard.html')

def light_mode(request:HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', 'light')
    return response

def dark_mode(request:HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', 'dark')
    return response
