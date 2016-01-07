# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160105_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.CharField(max_length=20000),
        ),
    ]
