# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunbo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': '蘑菇街_轮播图',
            },
        ),
    ]
