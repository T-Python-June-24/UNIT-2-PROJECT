from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def region(request):
    return render(request, 'region.html')

def yanboa(request):  
    return render(request, 'yanbu.html')

def nawras_island(request):
    return render(request, 'nawras_island.html')
def festival(request): 
    return render(request, 'festival.html')


