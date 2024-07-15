from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_view(request: HttpRequest):

    return render(request, "home.html")

def about_view(request: HttpRequest):
    pass

def cities_view(request: HttpRequest):
    pass

def agriculture_technologies_view(request: HttpRequest):
    pass



