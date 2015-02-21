# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0003_programme'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadCast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('blurb', models.TextField(blank=True)),
                ('channel', models.ForeignKey(blank=True, to='tv.Channel', null=True)),
                ('programme', models.ForeignKey(blank=True, to='tv.Programme', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
