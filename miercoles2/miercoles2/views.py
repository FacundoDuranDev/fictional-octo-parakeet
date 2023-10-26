from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        archivo = open("C:/Users/nubim/Documents/Proyectos/DJANGO MIERCOLES 2/miercoles2/miercoles2/templates/template1.html")
        
        return HttpResponse(archivo.read())