from django.urls import path
from . import viewsblog

urlpatterns = [

    path("", viewsblog.index, name="blogHome"),



]
