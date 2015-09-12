# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150912_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='legal_desc',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='organization',
            field=models.TextField(blank=True),
        ),
    ]
