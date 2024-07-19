from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AddToItineraryForm
from .models import ItineraryItem, Activity, Itinerary

def home(request):
    return render(request, 'home.html')

def WhatToDo(request):
    items = ItineraryItem.objects.all()
    context = {'items': items}
    return render(request, 'whattodo.html', context)


def PlanYourTrip(request):
    itinerary = request.session.get('itinerary', {})
    context = {'itinerary': itinerary}
    return render(request, 'planyourtrip.html', context)

def SaudiSeasons(request):
    return render(request, 'SaudiSeasons.html')

def SaudiMap(request):
    return render(request, 'SaudiMap.html')


def add_to_itinerary(request):
    if request.method == 'POST':
        form = AddToItineraryForm(request.POST)
        if form.is_valid():
            activity_id = form.cleaned_data['activity_id']
            activity = Activity.objects.get(id=activity_id)
            itinerary, created = Itinerary.objects.get_or_create(user=request.user)
            itinerary.activities.add(activity)
            if request.is_ajax():
                return JsonResponse({'status': 'success'})
            else:
                return redirect('PlanYourTrip')
    return JsonResponse({'status': 'error'}, status=400)

def what_to_do(request):
    natural_wonders = Activity.objects.filter(category='Natural Wonders')
    scuba_diving = Activity.objects.filter(category='Scuba Diving')
    mountains = Activity.objects.filter(category='Mountains')
    architecture_culture = Activity.objects.filter(category='Architecture and Culture')

    context = {
        'natural_wonders': natural_wonders,
        'scuba_diving': scuba_diving,
        'mountains': mountains,
        'architecture_culture': architecture_culture,
    }
    return render(request, 'WhatToDo.html', context)

