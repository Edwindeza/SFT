# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='trae_instrumento',
            field=models.BooleanField(default=False),
        ),
    ]
