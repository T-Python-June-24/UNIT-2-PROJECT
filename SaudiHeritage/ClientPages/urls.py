from . import views
from django.urls import path

NameApp="ClientPages"


urlpatterns=[
    path('' , views.index , name='index'),
    path('test/' , views.test , name='test'),
]