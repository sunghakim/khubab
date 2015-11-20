# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bab_img', models.FileField(null=True, upload_to=b'', blank=True)),
                ('bab_name', models.CharField(max_length=100)),
                ('bab_date', models.DateField()),
                ('bab_contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Spoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bab_number', models.IntegerField()),
                ('point_id', models.CharField(max_length=100)),
                ('point', models.IntegerField()),
            ],
        ),
    ]
