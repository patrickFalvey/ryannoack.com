# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0006_auto_20150518_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='state',
            field=models.CharField(default=b'none', max_length=50),
        ),
    ]
