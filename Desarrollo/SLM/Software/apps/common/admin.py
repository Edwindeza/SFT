from django.contrib import admin

from .models import Distrito, Provincia, Departamento


admin.site.register(Departamento)
admin.site.register(Provincia)
admin.site.register(Distrito)
