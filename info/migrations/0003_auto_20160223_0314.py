# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_videos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]
