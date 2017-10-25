from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel, Distrito


class TipoInstrumento(BaseModel):
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tipo de Instrumento'
        verbose_name_plural = 'Tipos de Instrumentos'


class Instrumento(BaseModel):
    nombre = models.CharField(max_length=30)
    tipo = models.ForeignKey(TipoInstrumento)

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'


def subir_foto_instrumento(instance, filename):
    ext = filename.split('.')[-1]
    filename = "instrumento_{0}.{1}".format(timezone.now(), ext)
    return "%s/%s" % (instance._meta.app_label, filename)


class InstrumentoRegistrado(BaseModel):
    instrumento = models.ForeignKey(Instrumento)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    foto = models.ImageField(upload_to=subir_foto_instrumento)

    class Meta:
        verbose_name = 'Instrumento registrado'
        verbose_name_plural = 'Instrumentos registrados'


def subir_foto_local(instance, filename):
    ext = filename.split('.')[-1]
    filename = "local_{0}.{1}".format(timezone.now(), ext)
    return "%s/%s" % (instance._meta.app_label, filename)


class Local(BaseModel):
    nombre = models.CharField(max_length=50)
    distrito = models.ForeignKey(Distrito)
    direccion = models.CharField(max_length=200)
    aforo = models.PositiveIntegerField()
    foto = models.ImageField(upload_to=subir_foto_local)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'


class TipoDocumento(BaseModel):
    nombre = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class GeneroMusical(BaseModel):
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Genero musical'
        verbose_name_plural = 'Generos musicales'


class Cliente(BaseModel):
    nombres = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    tipo_doc = models.ForeignKey(TipoDocumento)
    nro_doc = models.CharField(max_length=12)
    distrito = models.ForeignKey(Distrito)
    direccion = models.CharField(max_length=50, null=True, blank=True)

    artista_favorito = models.CharField(max_length=80, null=True, blank=True)
    genero_favorito = models.ForeignKey(GeneroMusical, null=True)
    instrumento_favorito = models.ForeignKey(Instrumento, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Reserva(BaseModel):
    EN_ESPERA = 0
    APROBADO = 1
    RECHAZADO = 2
    CANCELADO = 3
    FINALIZADO = 4

    ESTADOS = (
        (EN_ESPERA, 'En espera'),
        (APROBADO, 'Aprobado'),
        (RECHAZADO, 'Rechazado'),
        (CANCELADO, 'Cancelado'),
        (FINALIZADO, 'Finalizado')
    )

    cliente = models.ForeignKey(Cliente)
    local = models.ForeignKey(Local)
    cantidad_personas = models.PositiveIntegerField()
    estado = models.PositiveIntegerField(choices=ESTADOS, default=EN_ESPERA)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    instrumentos = models.ManyToManyField(InstrumentoRegistrado)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
