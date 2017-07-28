# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20170720_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobedone',
            name='deadline',
            field=models.DateField(),
        ),
    ]
