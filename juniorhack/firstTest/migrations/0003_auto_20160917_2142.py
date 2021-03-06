# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTest', '0002_auto_20160917_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openconversations',
            name='people',
        ),
        migrations.RemoveField(
            model_name='people',
            name='host',
        ),
        migrations.RemoveField(
            model_name='people',
            name='person1',
        ),
        migrations.RemoveField(
            model_name='people',
            name='person2',
        ),
        migrations.RemoveField(
            model_name='people',
            name='person3',
        ),
        migrations.RemoveField(
            model_name='people',
            name='person4',
        ),
        migrations.AddField(
            model_name='person',
            name='desiredTopic',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='distance',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='sexuality',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='OpenConversations',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
