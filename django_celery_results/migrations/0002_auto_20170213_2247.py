# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='task_arguments',
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='task_name',
            field=models.CharField(db_index=True, editable=False, max_length=256, null=True),
        ),
    ]
