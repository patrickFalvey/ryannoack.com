# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0005_gun_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gig_date', models.DateTimeField(verbose_name=b'Date')),
                ('venue', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Gun',
        ),
    ]
