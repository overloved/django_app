# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_type_id', models.IntegerField(default=b'0', max_length=2)),
                ('group_id', models.IntegerField(default=b'0', max_length=2)),
                ('fname', models.CharField(default=b'', max_length=30)),
                ('lname', models.CharField(default=b'', max_length=30)),
                ('sex', models.CharField(default=b'', max_length=1)),
                ('date_of_birth', models.CharField(default=b'', max_length=10)),
                ('address_1', models.CharField(default=b'', max_length=255)),
                ('address_2', models.CharField(default=b'', max_length=30)),
                ('city', models.CharField(default=b'', max_length=255)),
                ('region', models.CharField(default=b'', max_length=255)),
                ('country', models.CharField(default=b'', max_length=255)),
                ('zipcode', models.CharField(default=b'', max_length=255)),
                ('email', models.EmailField(default=b'', max_length=255)),
                ('username', models.CharField(default=b'', max_length=30)),
                ('password', models.CharField(default=b'', max_length=30)),
                ('phone', models.CharField(default=b'', max_length=20)),
                ('image', models.CharField(default=b'', max_length=255)),
                ('is_active', models.BooleanField(default=b'1')),
                ('recent_ip', models.CharField(default=b'', max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
