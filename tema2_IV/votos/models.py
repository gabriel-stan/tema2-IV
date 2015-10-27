from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(primary_key=True, max_length=200)

    def get_media(self):
        media = 0.0
        all_calificaciones = Calificacion.objects.filter(empresa = self)

        for cal in all_calificaciones:
            media += cal.calificacion

        media /= all_calificaciones.count()

        return media



class Calificacion(models.Model):
    empresa = models.ForeignKey(Empresa)
    calificacion = models.IntegerField()