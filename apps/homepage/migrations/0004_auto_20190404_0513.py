# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20190404_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='Bio',
            field=models.CharField(max_length=500, default=datetime.datetime(2019, 4, 4, 2, 12, 1, 272430, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='Contacts',
            field=models.CharField(max_length=500, default=datetime.datetime(2019, 4, 4, 2, 12, 7, 979097, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='Email',
            field=models.EmailField(max_length=254, default=datetime.datetime(2019, 4, 4, 2, 12, 52, 937282, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='Jabber',
            field=models.CharField(max_length=50, default=datetime.datetime(2019, 4, 4, 2, 13, 2, 181412, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='Skype',
            field=models.CharField(max_length=50, default=datetime.datetime(2019, 4, 4, 2, 13, 5, 912079, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='bDate',
            field=models.DateField(default=datetime.datetime(2019, 4, 4, 2, 13, 9, 853044, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human',
            name='sName',
            field=models.CharField(max_length=50, default=datetime.datetime(2019, 4, 4, 2, 13, 13, 665672, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
