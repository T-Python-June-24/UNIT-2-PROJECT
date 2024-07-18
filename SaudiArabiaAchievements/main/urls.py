from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home,name='home'),
    path('/dark',views.dark_mode,name='dark_mode'),
    path('/light',views.light_mode,name='light_mode'),
    path('/achievements',views.achievements,name='achievements'),
    path('/projects',views.projects,name='projects'),
    path('/award',views.award,name='award'),
    path('/contact',views.contact,name='contact'),
]