# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20170301_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='recommend',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe6\x9c\x8d'),
        ),
    ]