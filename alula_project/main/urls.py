from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heritage/', views.heritage, name='heritage'),
    path('nature/', views.nature, name='nature'),
    path('events/', views.events, name='events'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('dining/', views.dining, name='dining'),
    path('dining/<int:pk>/', views.dining_detail, name='dining_detail'),
    path('accommodation_list/', views.accommodation_list, name='accommodation_list'),
    path('accommodation_list/<int:pk>/', views.accommodation_detail, name='accommodation_detail'),
]
