# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0007_auto_20180301_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_type',
            field=models.CharField(default='\u524d\u7aef\u5b89\u5168', max_length=20, choices=[(0, '\u524d\u7aef\u5b89\u5168'), (1, '\u540e\u7aef\u6e17\u900f'), (2, '\u6f0f\u6d1e\u5206\u6790'), (3, '\u593a\u65d7\u7ade\u8d5b'), (4, '\u795e\u5668\u5206\u4eab'), (5, '\u7a0b\u5e8f\u4e4b\u7f8e')]),
        ),
    ]
