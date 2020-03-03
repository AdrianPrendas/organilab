# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import printOrderManager.validators


class Migration(migrations.Migration):

    dependencies = [
        ('printOrderManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='printobject',
            name='phone',
            field=models.TextField(default='', max_length=15, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='printobject',
            name='email',
            field=models.EmailField(max_length=254, validators=[printOrderManager.validators.validate_email], verbose_name='Email address'),
        ),
    ]