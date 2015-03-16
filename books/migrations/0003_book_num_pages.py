# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150313_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
