from django.shortcuts import render ,redirect
from django.http import HttpRequest ,HttpResponse 

def home(request:HttpRequest):

    return render(request,'main/home.html')


def achievements(request:HttpRequest):

    return render(request,'main/achievements.html')


def dark_mode(request:HttpRequest):

    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.set_cookie("mode","dark",max_age=60*60*24*7)

    return response

def light_mode(request:HttpRequest):

    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.delete_cookie("mode")

    return response

