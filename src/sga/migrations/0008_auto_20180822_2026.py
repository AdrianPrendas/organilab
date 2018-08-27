# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0007_auto_20180822_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prudenceadvice',
            options={'permissions': (('view_prudenceadvice', 'Can see available prudence advice'),), 'verbose_name': 'Prudence Advice', 'verbose_name_plural': 'Prudence Advices'},
        ),
        migrations.AddField(
            model_name='prudenceadvice',
            name='code',
            field=models.CharField(default='', max_length=150, verbose_name='Code'),
            preserve_default=False,
        ),
    ]