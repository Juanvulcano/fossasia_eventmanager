# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160102_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='events_assisted',
            field=models.IntegerField(null=True, verbose_name='Events already assisted'),
        ),
    ]
