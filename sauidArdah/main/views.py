from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse 

# Create your views here.

def home_view(request:HttpRequest)->render:
    return render(request,"main/index.html")

def change_theme(request: HttpRequest) -> HttpResponse:
    response = redirect(request.GET.get("next", "/"))
    # the default is light mode.
    if "dark_theme" not in request.COOKIES:
        response.set_cookie("dark_theme", "true")
    else:  
        current_value = request.COOKIES.get("dark_theme")
        if current_value == "true":
            
            response.set_cookie("dark_theme", "false")
        else:
            
            response.set_cookie("dark_theme", "true")
    
    return response

def njdiArdah_view(request:HttpRequest)->render:
    poets=[{
        "name":"Naser Alorainee",
        "img":"images/naserAlareeni.jpg",
        "city":"al diriyah"

    },
    {
        "name":"Abdullah Alsobai",
        "img":None,
        "city":"Shaqra"
    },
    {
        "name":"Mohammed Aloani",
        "img":"images/mohammedAloanii.jpg",
        "city":"alrabieia"
    },
    {
        "name":"Fhaed bin Dhaemm",
        "img":None,
        "city":"Riyadh"
    },
    {
        "name":"Abdurhman Alboardi",
        "img":None,
        "city":"Shaqra"
    }
    ]
    return render(request,"main/njdiArdah.html",context={"poets":poets})