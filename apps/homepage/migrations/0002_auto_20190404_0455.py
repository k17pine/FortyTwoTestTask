# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='Bio',
        ),
        migrations.RemoveField(
            model_name='human',
            name='Contacts',
        ),
        migrations.RemoveField(
            model_name='human',
            name='Jabber',
        ),
        migrations.RemoveField(
            model_name='human',
            name='bDate',
        ),
    ]
