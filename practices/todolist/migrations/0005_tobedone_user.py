# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20170722_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='tobedone',
            name='user',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
