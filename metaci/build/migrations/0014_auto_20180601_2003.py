# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-01 20:03
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import metaci.build.models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0013_auto_20180508_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowtask',
            name='exception_value',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=metaci.build.models.GnarlyEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='flowtask',
            name='options',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=metaci.build.models.GnarlyEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='flowtask',
            name='result',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=metaci.build.models.GnarlyEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='flowtask',
            name='return_values',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=metaci.build.models.GnarlyEncoder, null=True),
        ),
    ]
