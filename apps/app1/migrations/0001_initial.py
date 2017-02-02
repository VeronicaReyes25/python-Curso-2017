# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=20)),
                ('anio', models.IntegerField(default=2000)),
                ('dechaAdquisicion', models.DateField()),
            ],
        ),
    ]