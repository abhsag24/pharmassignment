# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmeasyflow', '0007_auto_20170813_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(to='pharmeasyflow.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pharmacist',
            field=models.ManyToManyField(to='pharmeasyflow.Pharmacist'),
        ),
    ]
