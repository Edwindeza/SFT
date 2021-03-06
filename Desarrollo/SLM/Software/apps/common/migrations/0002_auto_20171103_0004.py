# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='codigo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='distrito',
            name='codigo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='provincia',
            name='codigo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincia', to='common.Provincia'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='common.Departamento'),
        ),
    ]
