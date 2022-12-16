from django.contrib import admin
from django.urls import path
from appweather import views

urlpatterns = [
    path("", views.index, name="home"),
]
