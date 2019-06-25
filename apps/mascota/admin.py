from django.contrib import admin

from apps.mascota.models import vacuna, mascota

# Register your models here.

admin.site.register(vacuna)
admin.site.register(mascota)