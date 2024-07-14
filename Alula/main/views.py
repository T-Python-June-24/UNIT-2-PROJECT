# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import Place, Event, Experience

def home(request):
    places = Place.objects.all()
    events = Event.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'main/home.html', {'places': places, 'events': events, 'experiences': experiences})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'main/place_detail.html', {'place': place})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'main/event_detail.html', {'event': event})

def experience_detail(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    return render(request, 'main/experience_detail.html', {'experience': experience})
