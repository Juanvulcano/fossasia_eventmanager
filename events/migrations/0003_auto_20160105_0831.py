# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160103_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
