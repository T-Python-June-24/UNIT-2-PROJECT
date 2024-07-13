
from django.urls import path
from . import views


app_name = 'Tourister'

urlpatterns = [
    
    path('', views.home, name='home'),
    
]
