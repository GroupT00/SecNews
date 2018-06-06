# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0004_auto_20180228_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_click',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_url',
            field=models.CharField(max_length=255),
        ),
    ]
