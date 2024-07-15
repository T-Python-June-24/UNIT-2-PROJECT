# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


properties = [
    {"title": "Riyadh", "content": "Experience Riyadh, Saudi Arabia's vibrant capital and largest city, set amidst the desert on the Najd plateau. Renowned for its pivotal role since the 1950s, Riyadh captivates with its political, administrative, and economic importance, embodying the essence of modern Arabian dynamism.", "image": "riyadh.jpg","link":"https://en.wikipedia.org/wiki/Riyadh"},
    {"title": "Makkah","content": "Discover Mecca, Islam's holiest city and birthplace of Prophet Muhammad. With a population of 2.39 million in 2022, it is where the Quran was first revealed. Experience the spiritual essence of Mecca, home to the sacred Masjid al-Haram, the holiest mosque in Islam. offering a rich blend of spiritual and historical experiences.", "image": "makkah.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Madinah","content": "Medina, or Al-Madinah al-Munawwarah, is a city of profound Islamic heritage, centered around Al-Masjid al-Nabawi, the mosque built by Prophet Muhammad. It's a key pilgrimage site with historical landmarks like Mount Uhud and the Quba Mosque, offering a rich blend of spiritual and historical experiences.", "image": "madinah.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Jeddah","content": "Discover Jeddah, Saudi Arabia's bustling port city nestled along the Red Sea coast. Serving as the gateway to Mecca and Medina, Jeddah boasts a vibrant population of about 3.75 million. Renowned for its commercial significance, rich seafood culture, and popularity as a resort destination, Jeddah offers a vibrant blend of commerce and leisure", "image": "jed.jpg","link":"https://en.wikipedia.org/wiki/Jeddah"},
    {"title": "Al-Bahah","content": "Explore Al Baha, nestled in the picturesque Sarawat Mountains of southwestern Saudi Arabia. With its delightful climate and lush surrounding forests, Al Baha beckons as a premier tourist destination. Serving as the capital of the Al Bahah Region, it offers a serene retreat amidst natural beauty.", "image":"bahah.jpeg","link":"https://en.wikipedia.org/wiki/Al_Bahah"},
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



