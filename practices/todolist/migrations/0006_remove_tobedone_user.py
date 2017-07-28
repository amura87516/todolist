# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_tobedone_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tobedone',
            name='user',
        ),
    ]
