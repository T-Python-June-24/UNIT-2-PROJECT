from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.


def index(request:HttpRequest):
    return render(request , 'index.html')

def base(request:HttpRequest):
    return render(request , 'test.html')


def light_mode(request:HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', 'light')
    return response

def dark_mode(request:HttpRequest):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('mode', 'dark')
    return response
