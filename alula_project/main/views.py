from django.shortcuts import render
from .models import HeritageSite, NatureActivity, Event, Accommodation, Dining

def index(request):
    return render(request, 'main/index.html')

def heritage(request):
    sites = HeritageSite.objects.all()
    return render(request, 'main/heritage.html', {'sites': sites})

def nature(request):
    activities = NatureActivity.objects.all()
    return render(request, 'main/nature.html', {'activities': activities})

def events(request):
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events': events})

def accommodation(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'main/accommodation.html', {'accommodations': accommodations})

def dining(request):
    dining_places = Dining.objects.all()
    return render(request, 'main/dining.html', {'dining_places': dining_places})
