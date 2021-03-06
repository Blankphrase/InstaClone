# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20180723_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile_det',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=300),
        ),
    ]
