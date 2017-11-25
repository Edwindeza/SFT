from django.contrib import admin

from .models import Distrito, Provincia, Departamento


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Provincia)
class ServiciosAdmin(admin.ModelAdmin):
    pass


@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    pass
