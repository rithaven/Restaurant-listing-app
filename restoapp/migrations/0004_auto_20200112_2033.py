# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-12 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0003_auto_20200112_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restorent',
            name='restorentImg',
            field=models.ImageField(null=True, upload_to='locations/'),
        ),
    ]
