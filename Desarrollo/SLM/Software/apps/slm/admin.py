from django.contrib import admin

from .models import (
    TipoDocumento,
    TipoInstrumento,
    Instrumento,
    Local,
    Cliente,
    GeneroMusical,
    InstrumentoRegistrado
)


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(TipoInstrumento)
class TipoInstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo']
    list_filter = ['tipo']


@admin.register(InstrumentoRegistrado)
class InstrumentoRegistradoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'instrumento']


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'distrito', 'direccion', 'aforo']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellido_paterno',
        'apellido_materno',
        'tipo_doc',
        'distrito',
        'direccion',]


@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    pass
