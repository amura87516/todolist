# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170720_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tobedone',
            name='finished',
        ),
        migrations.AddField(
            model_name='tobedone',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
