from django.shortcuts import render
from django.views import View
import random
# Create your views here.

class RandomFacts(View):
    def get(self, request):
        refranes_espanol = [
            "Más vale tarde que nunca.",
            "No hay mal que por bien no venga.",
            "A quien madruga, Dios le ayuda.",
            "En boca cerrada no entran moscas.",
            "El que mucho abarca, poco aprieta."
        ]
        random_fact = random.choice(refranes_espanol)
        return render(request, "random_facts.html", {
            "random_fact": random_fact
        })
