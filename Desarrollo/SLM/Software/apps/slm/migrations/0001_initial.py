# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 20:25
from __future__ import unicode_literals

import apps.slm.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombres', models.CharField(max_length=80)),
                ('apellido_paterno', models.CharField(max_length=40)),
                ('apellido_materno', models.CharField(max_length=40)),
                ('nro_doc', models.CharField(max_length=12)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('artista_favorito', models.CharField(blank=True, max_length=80, null=True)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Distrito')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='GeneroMusical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Genero musical',
                'verbose_name_plural': 'Generos musicales',
            },
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Instrumento',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
        migrations.CreateModel(
            name='InstrumentoRegistrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to=apps.slm.models.subir_foto_instrumento)),
                ('instrumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slm.Instrumento')),
            ],
            options={
                'verbose_name': 'Instrumento registrado',
                'verbose_name_plural': 'Instrumentos registrados',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('aforo', models.PositiveIntegerField()),
                ('foto', models.ImageField(upload_to=apps.slm.models.subir_foto_local)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Distrito')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('cantidad_personas', models.PositiveIntegerField()),
                ('estado', models.PositiveIntegerField(choices=[(0, 'En espera'), (1, 'Aprobado'), (2, 'Rechazado'), (3, 'Cancelado'), (4, 'Finalizado')], default=0)),
                ('fecha_reserva', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slm.Cliente')),
                ('instrumentos', models.ManyToManyField(to='slm.InstrumentoRegistrado')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slm.Local')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documentos',
            },
        ),
        migrations.CreateModel(
            name='TipoInstrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo de Instrumento',
                'verbose_name_plural': 'Tipos de Instrumentos',
            },
        ),
        migrations.AddField(
            model_name='instrumento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slm.TipoInstrumento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='genero_favorito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='slm.GeneroMusical'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='instrumento_favorito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='slm.Instrumento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slm.TipoDocumento'),
        ),
    ]