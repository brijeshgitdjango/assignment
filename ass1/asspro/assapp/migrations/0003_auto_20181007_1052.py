# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-07 05:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assapp', '0002_auto_20181007_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institute',
            old_name='trainerr',
            new_name='trainer',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='employeee',
            new_name='employee',
        ),
    ]
