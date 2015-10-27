# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='califiacion',
            new_name='media_calificacion',
        ),
    ]
