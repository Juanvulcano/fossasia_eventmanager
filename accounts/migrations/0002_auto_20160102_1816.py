# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'attendee',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'organizer',
            },
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='events_assisted',
            field=models.IntegerField(verbose_name='Events already assisted'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='profile',
            field=models.ForeignKey(to='accounts.MyProfile'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='profile',
            field=models.ForeignKey(to='accounts.MyProfile'),
        ),
    ]
