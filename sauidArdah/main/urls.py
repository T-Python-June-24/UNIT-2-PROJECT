from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_view,name="home_view"),
    path("changeTheme/",views.change_theme,name="change_theme"),
    path("njdi/ardah/",views.njdiArdah_view,name="njdiArdah_view"),
    path("south/ardah/",views.southArdah_view,name="southArdah_view")
]
