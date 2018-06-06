# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0002_auto_20180228_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
