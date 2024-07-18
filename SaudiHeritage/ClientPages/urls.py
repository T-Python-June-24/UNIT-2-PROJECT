from . import views
from django.urls import path

app_name= 'ClientPages'


urlpatterns=[
    path('' , views.index , name='index'),
    path('Regions/' , views.Regions , name='Regions'),
    path('dark-mode/', views.dark_mode , name='dark'),
    path('light-mode/' , views.light_mode , name='light'),
    path('RjalAlma/' , views.RjalAlma, name='RjalAlma'),
    path('alanga/' , views.alanga, name='alanga'),
    path('mard/' , views.mard, name='mard'),
]