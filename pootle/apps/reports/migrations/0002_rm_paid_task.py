# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paidtask',
            name='user',
        ),
        migrations.DeleteModel(
            name='PaidTask',
        ),
    ]
