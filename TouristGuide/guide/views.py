from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request: HttpRequest):
    response = render(request, 'guide/home.html')
    #response.set_cookie('name','value')
    return response

def pictures(request: HttpRequest):
    pictures = [
        {"title" : "Nice picure", "image" : "1.jpg"},
        {"title" : "Really captivating landscape", "image" : "2.jpg"},
        {"title" : "Nice pic", "image" : "3.jpg"},
        {"title" : "Good photos", "image" : "4.jpg"},
    ]
    return render(request, 'guide/pictures.html', context={'pictures': pictures})

def darkMode(request:HttpRequest):
    response = redirect("guide:home")
    response.set_cookie("mode","dark",max_age=60*60*24)
    return response

def lightMode(request:HttpRequest):
    response = redirect("guide:home")
    response.set_cookie("mode","light",max_age= -3600)
    return response