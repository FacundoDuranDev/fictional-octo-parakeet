from django.shortcuts import render
from django.views import View
# Create your views here.

class Agregar(View):
    def get(self, request, nombre):
        with open("registros.txt", "a") as archivo:
            archivo.write(nombre + ",")
        return render(request, "agregar.html", {
            "nombre": nombre
        })

class Eliminar(View):
    def get(self, request, nombre):
        with open("registros.txt", "r") as archivo:
            raw_string = archivo.read()
            archivo.close()

        with open("registros.txt", "w") as archivo:
            archivo.write(raw_string.replace(nombre + ",",""))
            archivo.close()
        return render(request, "eliminar.html", {
            "nombre": nombre
        })


class Entregar(View):
    def get(self, request):
        with open("registros.txt", "r") as archivo:
            raw_string = archivo.read()
            archivo.close()
        nombres = raw_string.split(",")
        return render(request, "entregar.html", {
            "nombres": nombres
        })