from django.urls import path
from . import views


app_name = "guide"
urlpatterns = [
    path('',views.home, name= "home"),
    path('pictures/',views.pictures, name= "pictures"),
    
    path('darkMode/',views.darkMode, name= 'darkMode'),
    path('lightMode/',views.lightMode, name= 'lightMode'),
]