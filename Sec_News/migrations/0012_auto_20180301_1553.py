# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sec_News', '0011_auto_20180301_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newssql',
            name='Art_click',
            field=models.CharField(default=0, max_length=10, verbose_name='\u70b9\u51fb\u91cf'),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_exa',
            field=models.BooleanField(default=True, verbose_name='\u53d1\u5e03'),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_title',
            field=models.CharField(max_length=255, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_type',
            field=models.IntegerField(max_length=20, verbose_name='\u5206\u7c7b', choices=[(0, '\u524d\u7aef\u5b89\u5168'), (1, '\u540e\u7aef\u6e17\u900f'), (2, '\u6f0f\u6d1e\u5206\u6790'), (3, '\u593a\u65d7\u7ade\u8d5b'), (4, '\u795e\u5668\u5206\u4eab'), (5, '\u7a0b\u5e8f\u4e4b\u7f8e')]),
        ),
        migrations.AlterField(
            model_name='newssql',
            name='Art_url',
            field=models.CharField(max_length=255, verbose_name='\u94fe\u63a5'),
        ),
    ]
