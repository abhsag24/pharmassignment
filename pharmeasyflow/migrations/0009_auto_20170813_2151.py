# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmeasyflow', '0008_auto_20170813_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medical_record',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
