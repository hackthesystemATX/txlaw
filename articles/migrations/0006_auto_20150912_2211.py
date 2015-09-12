# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20150912_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='article',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 9, 12, 22, 11, 20, 786529, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
