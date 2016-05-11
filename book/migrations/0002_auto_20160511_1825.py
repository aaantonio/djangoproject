# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=50, blank=True, verbose_name='e-mail'),
        ),
    ]
