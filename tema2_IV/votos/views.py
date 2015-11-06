from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *


def index(request):
    todas_las_calificaciones = Calificacion.objects.all()
    context = {'ultimas_calificaciones': todas_las_calificaciones}
    return render(request, 'votos/index.html', context)

def calificar(request):
    return HttpResponse("You're looking at question.")

def results(request, empresa_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % empresa_id)