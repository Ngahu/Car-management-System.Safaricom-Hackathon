# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-09 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='edited',
            field=models.CharField(max_length=100),
        ),
    ]
