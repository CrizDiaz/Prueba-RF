from django.db import models

class persona(models.Model):
    #folio = models.CharField(default=1, max_length = 10,primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length = 12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
    Persona = models.ForeignKey(persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()