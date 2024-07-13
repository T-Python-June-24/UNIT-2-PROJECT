# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

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

def home(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            field_name = form.cleaned_data['field_name']
            field_value = form.cleaned_data['field_value']
            database.child(field_name).set(field_value)
            return redirect('Tourister:home')
    else:
        form = DataForm()

    firebase_data = database.get().val()

    return render(request, 'tourister/home.html', {
        'form': form,
        'firebase_data': firebase_data
    })
