# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("testresults", "0002_testresult_source_file")]

    operations = [
        migrations.RemoveField(model_name="testcodeunit", name="parent"),
        migrations.RemoveField(model_name="testcodeunit", name="testresult"),
        migrations.DeleteModel(name="TestCodeUnit"),
    ]
