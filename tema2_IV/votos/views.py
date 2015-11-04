from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *


def index(request):
    ultimas_calificaciones = Calificacion.objects.all()[:5]
    context = {'ultimas_calificaciones': ultimas_calificaciones}
    return render(request, 'votos/index.html', context)

def calificar(request):
    return HttpResponse("You're looking at question.")