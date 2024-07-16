from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heritage/', views.heritage, name='heritage'),
    path('nature/', views.nature, name='nature'),
    path('events/', views.events, name='events'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('dining/', views.dining, name='dining'),
]
