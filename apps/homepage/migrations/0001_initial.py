# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=50)),
                ('sName', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Skype', models.CharField(max_length=50)),
                ('Jabber', models.CharField(max_length=50)),
                ('bDate', models.DateField()),
                ('Bio', models.CharField(max_length=500)),
                ('Contacts', models.CharField(max_length=500)),
            ],
        ),
    ]
