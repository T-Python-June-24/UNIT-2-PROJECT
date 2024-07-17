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
    
    {"title": "Riyadh", "content": "Riyadh combines ancient history with modern dynamism, offering a glimpse into Arabia’s past and future. Explore the city's rich heritage through souqs, museums, and historical architecture, and experience its modern side with high-rises and a thriving art scene, highlighted by the Riyadh Art initiative that turns the city into an open-air gallery. Don't miss Riyadh Season, featuring themed zones like Boulevard City and the Riyadh Zoo, open year-round. For dining, try local delicacies at Najd Village restaurant.", "image": "riyadh.jpg","link":"https://en.wikipedia.org/wiki/Riyadh"},
    {"title": "Makkah","content": "Makkah, the birthplace of Prophet Muhammad and where the Quran was revealed, is a pivotal city in Islam. It hosts the annual Hajj pilgrimage, one of the five pillars of Islam, and welcomes millions for the Umrah pilgrimage year-round. Key sites include Al Masjid Al Haram, the largest mosque in the world, and the historic Masjid-e-Aisha. Beyond its spiritual significance, visitors can explore the Makkah Museum's pre-Islamic artifacts or shop and play at Makkah Mall.", "image": "makkah1.jpg","link":"https://en.wikipedia.org/wiki/Mecca"},
    {"title": "Madinah","content": "Madinah, one of Islam's two holiest cities, attracts millions of pilgrims annually for Hajj or Umrah. Central to the city is Al Masjid an Nabawi, also known as the Prophet’s Mosque, built by the Prophet Muhammad in 622 A.D. and his burial site. Other highlights include Quba Mosque, Islam's first mosque, and the historic Mount Uhud. Visitors can also explore the Hijaz Railway Museum to learn about the old railway that connected Damascus with Makkah and Madinah, or take the modern Haramain High-Speed Railway between Madinah and Makkah.", "image": "madinah.jpg","link":"https://en.wikipedia.org/wiki/Medina"},
    {"title": "Jeddah","content": "Experience the charm of Jeddah’s heritage as you wander through the historic streets of Al Balad. Discover a shopping paradise at the Mall of Arabia and Red Sea Mall. Dive into the refreshing waters of the Red Sea or take a leisurely stroll along the Jeddah Corniche. Don't miss the spectacular King Fahd Fountain, a marvel that shoots water 312 meters into the sky.", "image": "jed.jpg","link":"https://en.wikipedia.org/wiki/Jeddah"},
    {"title": "Dammam","content": "Dammam, a vibrant port city in Saudi Arabia's Eastern Province, offers more than just its famous port. Enjoy the serene Arabian Gulf views, stroll along the Dammam Corniche, or visit the lush King Fahad Park, one of Saudi's largest. Explore Al Marjan Island, Saudi's first man-made island, or relax at Half Moon Bay. The city is becoming a hub for entertainment, with options ranging from movies at Ithra in Dhahran to shopping at Othaim Mall or the Dammam Souq, where local crafts and jewelry abound.", "image":"dammam.jpg","link":"https://en.wikipedia.org/wiki/Dammam"},
    {"title": "Al-Bahah","content": "A journey to Al Baha is a unique experience in Saudi, contrasting its typical desert landscape with historic towers, lush forests, and cool climates. At 2,500 meters above sea level, it's perfect for outdoor activities like hiking and camping. Highlights include the Raghdan Forest Park, Shada Mountains, ancient caves, the marble village of Dhee Ayn, Al Kharrarah Waterfall, and Prince Hussam Park with its interactive water features and children’s area.", "image":"bahah.jpeg","link":"https://en.wikipedia.org/wiki/Al_Bahah"},
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
