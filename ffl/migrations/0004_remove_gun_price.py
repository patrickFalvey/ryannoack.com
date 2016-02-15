# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0003_auto_20150517_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gun',
            name='price',
        ),
    ]
