from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_view,name="home_view"),
    path("changeTheme/",views.change_theme,name="change_theme"),
    path("njdi/ardah/",views.njdiArdah_view,name="njdiArdah_view"),
    path("south/ardah/",views.southArdah_view,name="southArdah_view"),
    path("qazwai/ardah/",views.qazwaiArdah_view,name="qazwaiArdah_view"),
    path("daha/ardah",views.dahaArdah,name="dahaArdah_view"),
    path("pictures/library/",views.picture_view,name="pictures_view"),
    path("about/us/",views.about_view,name="about_view"),
    path("contact/us",views.contact_view,name="contact_view")

]
