# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-15 11:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0011_auto_20170312_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='Title here', max_length=100)),
                ('Description', models.CharField(default='Description here', max_length=10000)),
                ('Link', models.CharField(default='Link here', max_length=100)),
                ('Postdate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
