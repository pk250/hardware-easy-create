# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-10-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware_department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parcen_id',
            field=models.IntegerField(),
        ),
    ]
