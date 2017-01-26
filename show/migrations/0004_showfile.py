# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-25 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20170126_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_id', models.IntegerField(default=0)),
                ('filename', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]