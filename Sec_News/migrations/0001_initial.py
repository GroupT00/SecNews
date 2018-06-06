# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSql',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Art_title', models.CharField(max_length=30)),
                ('Art_time', models.CharField(max_length=20)),
                ('Art_click', models.CharField(max_length=20)),
                ('Art_type', models.CharField(max_length=20)),
                ('Art_url', models.CharField(max_length=40)),
            ],
        ),
    ]
