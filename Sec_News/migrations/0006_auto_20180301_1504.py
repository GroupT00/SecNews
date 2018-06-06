# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0005_auto_20180301_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='newssql',
            name='Art_exa',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_title',
            field=models.CharField(max_length=50),
        ),
    ]
