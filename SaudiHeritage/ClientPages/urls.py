from . import views
from django.urls import path

app_name= 'ClientPages'


urlpatterns=[
    path('' , views.index , name='index'),
    path('test/' , views.base , name='test'),
    path('dark-mode/', views.dark_mode , name='dark'),
    path('light-mode' , views.light_mode , name='light'),
]