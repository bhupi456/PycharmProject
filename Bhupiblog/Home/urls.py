from django.urls import path
from . import views

urlpatterns = [

    path("", views.Home, name="Home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("Signup", views.Signup, name="Signup"),
    path("Login", views.Login, name="Login"),
    path("Logout", views.Logout, name="Logout"),


]
