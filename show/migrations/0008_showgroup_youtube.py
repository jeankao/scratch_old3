# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-15 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0007_auto_20170128_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='showgroup',
            name='youtube',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
