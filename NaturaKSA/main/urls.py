from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("city/Aseer/", views.Aseer, name="Aseer"),
     path("city/AlUla/", views.AlUla, name="AlUla"),
    path("city/AlUla/flamerace/", views.flameـrace, name="flameـrace"),
    path("city/Aseer/Sarawat/", views.Sarawat, name="Sarawat"),
    path("city/Aseer/Marka/", views.Marka, name="Marka"),
    path("mode/set/dark/", views.dark_mode, name="dark_mode"),
    path("mode/set/light/", views.light_mode, name="light_mode"),
   


]