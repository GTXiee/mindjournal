# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20171030_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='word_of_the_day_def',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='image',
            field=models.ImageField(null=True, upload_to='img/journalentries'),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='quote_author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='quote_content',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='word_of_the_day',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
