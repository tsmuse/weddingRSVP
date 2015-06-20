# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvpApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guest_attending',
            field=models.NullBooleanField(choices=[(None, 'No response'), (False, 'Not Attending'), (True, 'Attending')]),
        ),
        migrations.AlterField(
            model_name='guest',
            name='guest_drink_pref',
            field=models.NullBooleanField(choices=[(None, 'No alcohol'), (True, 'Beer'), (False, 'Wine')]),
        ),
    ]
