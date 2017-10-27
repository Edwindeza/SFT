from django.contrib import admin

from .models import TipoDocumento, TipoInstrumento, Instrumento, Local, Cliente, GeneroMusical


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoInstrumento)
class TipoInstrumentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    pass


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    pass
