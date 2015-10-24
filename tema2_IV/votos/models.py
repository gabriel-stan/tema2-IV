from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    califiacion = models.FloatField(default=0.0)

class Calificacion(models.Model):
    empresa = models.ForeignKey(Empresa);
    calificacion = models.FloatField()