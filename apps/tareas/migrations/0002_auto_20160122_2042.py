# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
