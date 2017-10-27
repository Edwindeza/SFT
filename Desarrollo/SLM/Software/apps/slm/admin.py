from django.contrib import admin

from .models import TipoDocumento, TipoInstrumento, Instrumento, Local, Cliente, GeneroMusical


admin.site.register(TipoDocumento)
admin.site.register(TipoInstrumento)
admin.site.register(Instrumento)
admin.site.register(Local)
admin.site.register(Cliente)
admin.site.register(GeneroMusical)
