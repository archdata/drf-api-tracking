# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0005_auto_20171219_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestlog',
            name='view',
            field=models.CharField(db_index=True, max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='view_method',
            field=models.CharField(db_index=True, max_length=27, blank=True, null=True),
        ),
    ]