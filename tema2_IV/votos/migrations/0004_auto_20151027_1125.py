# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0003_auto_20151027_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
