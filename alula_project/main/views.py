from django.shortcuts import render, get_object_or_404
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

def accommodation_list(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'main/accommodation_list.html', {'accommodations': accommodations})

def accommodation_detail(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    return render(request, 'main/accommodation_detail.html', {'accommodation': accommodation})

def dining_detail(request, pk):
    dining = get_object_or_404(Dining, pk=pk)
    return render(request, 'main/dining_detail.html', {'dining': dining})
