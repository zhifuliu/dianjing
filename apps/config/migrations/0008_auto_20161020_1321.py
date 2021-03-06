# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_auto_20160810_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadcast',
            name='server_max',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='server_min',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='display',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xbe\xe7\xa4\xba'),
        ),
    ]
