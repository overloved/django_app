# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20150316_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 22, 41, 15, 193562)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userentity',
            name='password',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userentity',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 22, 41, 15, 193596)),
            preserve_default=True,
        ),
    ]
