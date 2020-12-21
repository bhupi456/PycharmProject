from django.urls import path
from . import viewsnews

urlpatterns = [
    path("", viewsnews.newsindex, name="newsHome"),

]

