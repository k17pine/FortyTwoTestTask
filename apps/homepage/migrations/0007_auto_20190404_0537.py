# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_delete_nothuman'),
    ]

    operations = [
        migrations.RenameField(
            model_name='human',
            old_name='bDate',
            new_name='bdate',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Bio',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Contacts',
            new_name='contacts',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Jabber',
            new_name='jabber',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='Skype',
            new_name='skype',
        ),
        migrations.RenameField(
            model_name='human',
            old_name='sName',
            new_name='sname',
        ),
    ]
