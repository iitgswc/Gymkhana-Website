# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0003_clubs_secy_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='secy_pic',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
