# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 18, 34, 7, 706014, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
