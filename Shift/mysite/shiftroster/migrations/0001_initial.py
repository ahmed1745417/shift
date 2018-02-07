# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('weekoff1', models.IntegerField()),
                ('weekoff2', models.IntegerField()),
                ('team', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('eid', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=200)),
            ],
        ),
    ]
