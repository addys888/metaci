# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-13 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("build", "0018_remove_build_schedule"),
        ("plan", "0016_auto_20180904_1457"),
    ]

    operations = [
        migrations.RemoveField(model_name="planschedule", name="branch"),
        migrations.RemoveField(model_name="planschedule", name="plan"),
        migrations.DeleteModel(name="PlanSchedule"),
    ]
