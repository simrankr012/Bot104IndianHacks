# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-04 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20170904_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalBeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bed_available', models.BooleanField(default=True)),
                ('room_type_a', models.IntegerField()),
                ('room_type_b', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Hospital')),
            ],
            options={
                'ordering': ['is_bed_available'],
            },
        ),
    ]
