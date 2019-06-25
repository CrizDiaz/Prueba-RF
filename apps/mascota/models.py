from django.db import models

from apps.adopcion.models import persona

class vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class mascota(models.Model):
    #folio = models.CharField(default=1, max_length = 10, primary_key = True)
    nombre = models.CharField(max_length = 50)
    sexo = models.CharField (max_length = 10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(vacuna,blank=True)