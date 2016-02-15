# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0004_remove_gun_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='gun',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
