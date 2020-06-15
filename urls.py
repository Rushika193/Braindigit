from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Hello world"),
   path("profile/", views.profile, name="profile page")
]

