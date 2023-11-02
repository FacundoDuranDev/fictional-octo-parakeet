from django.shortcuts import render
from django.views import View

class TestView(View):
    def get(self, request, variable):
        return render(request, "test.html", {
            "variable": variable
        })

class ListView(View):
    def get(self, request, variables):
        lista = variables.split(",")
        return render(request, "list.html", {
            "lista": lista
        })