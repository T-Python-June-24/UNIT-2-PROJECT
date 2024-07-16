import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import DataForm
import pyrebase
import os
from dotenv import load_dotenv
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

load_dotenv()  
openai_key = os.getenv("OPENAI_API_KEY")

llm_name = "gpt-3.5-turbo"
model = ChatOpenAI(api_key=openai_key, model=llm_name)

df = pd.read_csv("Tourister/static/data/data.csv").fillna(value=0)
agent_tool = create_pandas_dataframe_agent(llm=model, df=df, verbose=True)

CSV_PROMPT_SUFFIX = """
"""

properties = [
    
    {"title": "Riyadh", "content": "Experience Riyadh, Saudi Arabia's vibrant capital and largest city, set amidst the desert on the Najd plateau. Renowned for its pivotal role since the 1950s, Riyadh captivates with its political, administrative, and economic importance, embodying the essence of modern Arabian dynamism.", "image": "riyadh.jpg","link":"https://en.wikipedia.org/wiki/Riyadh"},
    {"title": "Makkah","content": "Discover Mecca, Islam's holiest city and birthplace of Prophet Muhammad. With a population of 2.39 million in 2022, it is where the Quran was first revealed. Experience the spiritual essence of Mecca, home to the sacred Masjid al-Haram, the holiest mosque in Islam. offering a rich blend of spiritual and historical experiences.", "image": "makkah.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Madinah","content": "Medina, or Al-Madinah al-Munawwarah, is a city of profound Islamic heritage, centered around Al-Masjid al-Nabawi, the mosque built by Prophet Muhammad. It's a key pilgrimage site with historical landmarks like Mount Uhud and the Quba Mosque, offering a rich blend of spiritual and historical experiences.", "image": "madinah.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Jeddah","content": "Discover Jeddah, Saudi Arabia's bustling port city nestled along the Red Sea coast. Serving as the gateway to Mecca and Medina, Jeddah boasts a vibrant population of about 3.75 million. Renowned for its commercial significance, rich seafood culture, and popularity as a resort destination, Jeddah offers a vibrant blend of commerce and leisure", "image": "jed.jpg","link":"https://en.wikipedia.org/wiki/Jeddah"},
    {"title": "Dammam","content": "Dammam, a vibrant port city in Saudi Arabia's Eastern Province, offers more than just its famous port. Enjoy the serene Arabian Gulf views, stroll along the Dammam Corniche, or visit the lush King Fahad Park, one of Saudi's largest. Explore Al Marjan Island, Saudi's first man-made island, or relax at Half Moon Bay. The city is becoming a hub for entertainment, with options ranging from movies at Ithra in Dhahran to shopping at Othaim Mall or the Dammam Souq, where local crafts and jewelry abound.", "image":"dammam.jpg","link":"https://en.wikipedia.org/wiki/Dammam"},
    {"title": "Al-Bahah","content": "Explore Al Baha, nestled in the picturesque Sarawat Mountains of southwestern Saudi Arabia. With its delightful climate and lush surrounding forests, Al Baha beckons as a premier tourist destination. Serving as the capital of the Al Bahah Region, it offers a serene retreat amidst natural beauty.", "image":"bahah.jpeg","link":"https://en.wikipedia.org/wiki/Al_Bahah"},
    {"title": "Taif","content": "Known as the City of Roses, Taif is famed for its fragrant roses and perfume factories. As Saudi's summer retreat, it offers a cool escape with highlights like the Souq Okaz festival and the Crown Prince Camel Festival in August. Key attractions include Al Hada Mountain, with its long cable car ride, rose fields, and trails, plus the Al Kar Tourist Village featuring a water park and toboggan slide. Various hotels and resorts reflect Taif's unique charm.", "image":"taif.jpg","link":"https://en.wikipedia.org/wiki/Taif"},
    {"title": "Qassim","content": "Located in Saudi’s central highlands, Qassim celebrates each year with the Buraydah Date Festival at the end of the harvest season. you should check out the Buraydah Museum for a glimpse into the history and culture of the region. Northwest of Buraydah lies the ancient oasis of Uyun Al Jiwa, which well-known Arab poets have cited in their work. At Al Bassam Heritage House, admire the many beautiful decorative patterns adorning this 3,500-square-meter Najdi-style palace.", "image":"qassim.jpg","link":"https://en.wikipedia.org/wiki/Al-Qassim_Province"},

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

def home(request: HttpResponse):
    return render(request, 'Tourister/home.html')

def home_light(request: HttpResponse):
    response = redirect('Tourister:home')
    response.delete_cookie('mode')  # !delete cookie 
    return response

def home_dark(request: HttpResponse):
    response = redirect('Tourister:home')
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)  # !cookie age
    return response

def kings(request: HttpResponse):
    return render(request, 'Tourister/kings.html')

def city(request: HttpResponse):
    return render(request, 'Tourister/city.html', context)

def contact(request: HttpResponse):
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

    return render(request, 'Tourister/contact.html', {
        'form': form,
        'firebase_data': firebase_data
    })

def card(request: HttpResponse):
    firebase_data = database.get().val()

    return render(request, 'Tourister/card.html', {
        'firebase_data': firebase_data
    })

def first_agent(messages):
    res = model.invoke(messages)
    return res

def agent(request: HttpResponse):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_input = body.get('message', '')

        if user_input:
            response = agent_tool.run(f"{user_input} {CSV_PROMPT_SUFFIX}")

            return JsonResponse({"response": response})

        return JsonResponse({"response": "No input provided."})

    return render(request, 'Tourister/agent.html')
