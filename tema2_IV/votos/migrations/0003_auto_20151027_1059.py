# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0002_auto_20151024_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='media_calificacion',
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='calificacion',
            field=models.IntegerField(),
        ),
    ]
