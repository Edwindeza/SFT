from django.db import models
from django.utils import timezone
from django.db.models import QuerySet


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class BaseModel(SoftDeletionModel):
    created_at = models.DateTimeField(blank=True, null=True, editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, editable=False, auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            self.modified_at = timezone.now()
        else:
            self.created_at = timezone.now()
            kwargs['force_insert'] = False
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Departamento(BaseModel):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre


class Provincia(BaseModel):
    nombre = models.CharField(max_length=40)
    departamento = models.ForeignKey(Departamento, related_name="departamento")
    codigo = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre


class Distrito(BaseModel):
    nombre = models.CharField(max_length=40)
    provincia = models.ForeignKey(Provincia, related_name="provincia")
    codigo = models.CharField(max_length=10, default='')

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'

    def __str__(self):
        return self.nombre
