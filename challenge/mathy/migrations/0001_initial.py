# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('sum_squares', models.PositiveIntegerField()),
                ('square_of_sum', models.PositiveIntegerField()),
                ('difference', models.IntegerField()),
                ('occurences', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
