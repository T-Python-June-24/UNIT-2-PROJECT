# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


properties = [
    {"title": "Makkah","content": "Mecca, the holiest city in Islam and capital of Mecca Province in Saudi Arabia, is the birthplace of Prophet Muhammad. It had a population of 2.39 million in 2022 and is where the Quran was first revealed. The city is home to the Masjid al-Haram, the holiest mosque in Islam.", "image": "makkah.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Riyadh", "content": "Riyadh is the capital and largest city of Saudi Arabia, located in the desert on the Najd plateau. It emerged as a major city after the 1950s and is known for its political, administrative, and economic significance.", "image": "riyadh.jpg","link":"https://en.wikipedia.org/wiki/Riyadh"},
    {"title": "Jeddah","content": "Jeddah is a major port city in Saudi Arabia, located on the Red Sea coast. It serves as the gateway to Mecca and Medina, with a population of about 3.75 million. Jeddah is known for its commercial importance, seafood culture, and as a popular resort destination.", "image": "jed.jpg","link":"https://en.wikipedia.org/wiki/Jeddah"},
    {"title": "Al-Bahah","content": "Al Baha is a city in southwestern Saudi Arabia, located in the Sarawat Mountains. It is known for its pleasant climate and surrounding forests, making it a prime tourist attraction. The city serves as the capital of Al Bahah Region.", "image":"bahah.jpeg","link":"https://en.wikipedia.org/wiki/Al_Bahah"},
]
context = {'properties': properties,}

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "databaseURL": os.getenv("DATABASE_URL"),
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

def home(request:HttpResponse):
   return render(request,'Tourister/home.html')




def home_light(request:HttpResponse):
    response = redirect('Tourister:home')
    response.delete_cookie('mode')#!cookie age 
    return response
    
    

def home_dark(request:HttpResponse):
    response = redirect('Tourister:home')
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)#!cookie age 
    return response



def kings(request:HttpResponse):
   return render(request,'Tourister/kings.html')



def city(request:HttpResponse):
       return render(request,'Tourister/city.html',context)


def contact(request:HttpResponse):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            field_name = form.cleaned_data['field_name']
            field_value = form.cleaned_data['field_value']
            database.child(field_name).set(field_value)
            return redirect('Tourister:contact')
    else:
        form = DataForm()

    firebase_data = database.get().val()

    return render(request, 'tourister/contact.html', {
        'form': form,
        'firebase_data': firebase_data
    })


def card(request:HttpResponse):
    firebase_data = database.get().val()

    return render(request, 'tourister/card.html', {
        'firebase_data': firebase_data
    })



