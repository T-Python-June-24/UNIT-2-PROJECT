from . import views
from django.urls import path


app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurants_view, name='restaurants'),
    path('recipe/<str:recipe_name>/', views.recipe_detail, name='recipe_detail'),
    path('regions/', views.regions, name='regions'),
]
