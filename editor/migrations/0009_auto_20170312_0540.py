# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0008_auto_20170312_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='about_us',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='achievements',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='contact',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='extra',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='past_events',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='projects',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='secy_details',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='up_events',
            field=models.CharField(blank=True, default='', max_length=50000),
        ),
    ]
