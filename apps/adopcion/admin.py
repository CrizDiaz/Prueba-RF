from django.contrib import admin

from apps.adopcion.models import persona, Solicitud

# Register your models here.
admin.site.register(persona)
admin.site.register(Solicitud)