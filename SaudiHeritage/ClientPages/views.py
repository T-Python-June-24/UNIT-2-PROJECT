from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.


def index(request:HttpRequest):
    return render(request , 'index.html')

def test(request:HttpRequest):
    return render(request , 'base.html')