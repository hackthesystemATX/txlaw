# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150912_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='approved',
            new_name='can_edit',
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
