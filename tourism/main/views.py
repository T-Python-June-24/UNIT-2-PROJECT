from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):

    response = render(request, "main/home.html")
    return response

def qatif(request: HttpRequest):

    return render(request, "main/qatif.html")

def riyadh(request: HttpRequest):

    return render(request, "main/riyadh.html")

def holy(request: HttpRequest):

    return render(request, "main/holy.html")

def jeddah(request: HttpRequest):

    return render(request, "main/jeddah.html")

def ahsa(request: HttpRequest):

    return render(request, "main/ahsa.html")

def ula(request: HttpRequest):

    return render(request, "main/ula.html")

def food(request: HttpRequest):

    return render(request, "main/food.html")

def light(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","light", max_age=60*60*24)
    return response

def dark(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","dark", max_age=60*60*24)
    return response
