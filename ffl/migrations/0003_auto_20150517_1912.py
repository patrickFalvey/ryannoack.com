# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0002_items_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='Gun',
        ),
        migrations.RenameField(
            model_name='gun',
            old_name='guns',
            new_name='gat',
        ),
    ]
