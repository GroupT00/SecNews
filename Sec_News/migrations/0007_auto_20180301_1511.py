# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0006_auto_20180301_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_title',
            field=models.CharField(max_length=255),
        ),
    ]
