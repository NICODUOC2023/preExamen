from django.contrib import admin
from .models import tipo_habitacion,reserva, Visitante
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(tipo_habitacion)
admin.site.register(reserva)
admin.site.register(Visitante)

