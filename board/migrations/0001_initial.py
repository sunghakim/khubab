# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('writer', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=70)),
                ('board_contents', models.TextField()),
                ('board_date', models.DateTimeField()),
            ],
        ),
    ]
