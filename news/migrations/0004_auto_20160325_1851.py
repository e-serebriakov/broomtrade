# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-25 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20160323_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 3, 25, 18, 51, 13, 728388), verbose_name='Опубликована'),
        ),
    ]
