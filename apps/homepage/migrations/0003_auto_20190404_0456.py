# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190404_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='human',
            name='Skype',
        ),
        migrations.RemoveField(
            model_name='human',
            name='sName',
        ),
    ]
