# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qsh', '0003_auto_20170402_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyable',
            name='last_use',
        ),
        migrations.RemoveField(
            model_name='buydetail',
            name='note',
        ),
    ]
