# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150912_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='hours',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='phone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
