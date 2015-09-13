# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20150912_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_major',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.TextField(blank=True),
        ),
    ]
