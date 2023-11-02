from django.contrib import admin
from django.urls import path
from .views import TestView, ListView

urlpatterns = [
    path("test/<str:variable>", TestView.as_view(), name="test"),
    path("list/<str:variables>", ListView.as_view(), name="list")
]
