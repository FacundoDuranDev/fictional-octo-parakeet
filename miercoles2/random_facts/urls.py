from django.contrib import admin
from django.urls import path, include
from .views import RandomFacts
urlpatterns = [
    path("", RandomFacts.as_view(), name="random_facts")
]