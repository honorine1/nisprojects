# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-03 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nisapp', '0009_auto_20191203_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='businessImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prodImage',
            new_name='image',
        ),
    ]