# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=100)),
                ('tweet', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=200)),
            ],
        ),
    ]
