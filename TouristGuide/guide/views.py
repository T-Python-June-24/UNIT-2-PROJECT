from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request: HttpRequest):
    response = render(request, 'guide/home.html')
    #response.set_cookie('name','value')
    return response


def explore(request: HttpRequest):
    response = render(request, 'guide/explore.html')
    return response


def pictures(request: HttpRequest):
    pictures = [
        {"title" : "Nice picure", "image" : "1.jpg"},
        {"title" : "Really captivating landscape", "image" : "2.jpg"},
        {"title" : "Nice pic", "image" : "3.jpg"},
        {"title" : "Good photos", "image" : "4.jpg"},
    ]
    return render(request, 'guide/pictures.html', context={'pictures': pictures})


def abha(request: HttpRequest):
    cities = [
        {"title" : '''Abha, the capital of Saudi Arabia's Asir Province, is a captivating tourist destination known
                    for its cool climate and stunning landscapes. Nestled in the Sarawat Mountains, Abha offers breathtaking 
                    views and lush greenery, making it a perfect escape from the desert heat. The city boasts numerous attractions,
                    including the Asir National Park, which is ideal for hiking and picnicking. The traditional mud-brick architecture
                    of Rijal Alma village and the vibrant Al-Muftaha Art Village reflect the region's rich cultural heritage. Abha's unique 
                    blend of natural beauty, pleasant weather, and cultural sites makes it a must-visit destination in Saudi Arabia.'''
         ,"images" : ["https://res.cloudinary.com/dirlusg8s/image/upload/v1721266521/abha2_hj76ct.jpg",
                        "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266519/abha1_z1tscl.jpg",
                        "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266519/abha3_m6uge7.png",
                        "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266516/abha4_nmbk3e.jpg",
         ]},
    ]
    return render(request, 'guide/abha.html', context={'cities': cities})

def jeddah(request: HttpRequest):
    cities = [
        {"title" : '''Jeddah, a bustling port city on the Red Sea, is a premier tourist destination in Saudi Arabia
          known for its vibrant culture and historical significance. The city's waterfront, the Jeddah Corniche,
          features beautiful beaches and art installations, perfect for leisurely strolls and family outings. Al-Balad, the historic old town, offers a glimpse into Jeddah's past with its ancient coral houses and bustling souks. The city is also famous for the King Fahd Fountain, the world's tallest, and its diverse culinary scene, blending traditional Saudi dishes with international flavors. With its mix of modern attractions and rich heritage, Jeddah captivates every traveler.'''
         ,"images" : ["https://res.cloudinary.com/dirlusg8s/image/upload/v1721266520/jed7_lelf1n.jpg",
                "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266520/jed3_utm79h.jpg",
                "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266518/jed6_wpxbu7.jpg",
                "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266519/jed5_zpxfak.png",
                "https://res.cloudinary.com/dirlusg8s/image/upload/v1721266518/jed1_po2fcb.jpg",

         ]},
    ]
    return render(request, 'guide/jeddah.html', context={'cities': cities})






def darkMode(request:HttpRequest):
    response = redirect("guide:home")
    response.set_cookie("mode","dark",max_age=60*60*24)
    return response

def lightMode(request:HttpRequest):
    response = redirect("guide:home")
    response.set_cookie("mode","light",max_age= -3600)
    return response