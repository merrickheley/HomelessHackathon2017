# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackApp', '0002_auto_20170603_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='accomodation_length',
            new_name='accommodation_length',
        ),
    ]
