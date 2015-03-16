# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentity',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 22, 12, 36, 357579)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userentity',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 22, 12, 36, 357612)),
            preserve_default=True,
        ),
    ]
