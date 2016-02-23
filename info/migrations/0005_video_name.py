# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20160223_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
