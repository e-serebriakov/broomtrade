# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Название')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'категория',
                'ordering': ['order', 'name'],
                'verbose_name_plural': 'категории',
            },
        ),
    ]