from django.urls import path
from . import views


app_name = "guide"
urlpatterns = [
    path('',views.home, name= "home"),
    path('pictures/',views.pictures, name= "pictures"),
    path('abha/',views.abha, name= "abha"),
    path('jeddah/',views.jeddah, name= "jeddah"),
     path('explore/',views.explore, name= "explore"),


    path('darkMode/',views.darkMode, name= 'darkMode'),
    path('lightMode/',views.lightMode, name= 'lightMode'),
]