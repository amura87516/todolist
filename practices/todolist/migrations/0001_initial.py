# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tobodone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('deadline', models.DateTimeField()),
                ('finished', models.BooleanField()),
            ],
        ),
    ]
