# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=150, unique=True, verbose_name='email'),
        ),
    ]
