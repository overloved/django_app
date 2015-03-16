# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150315_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 18, 22, 9, 390858)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userentity',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 18, 22, 9, 390895)),
            preserve_default=True,
        ),
    ]
