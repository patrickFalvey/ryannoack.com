# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20160223_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]
