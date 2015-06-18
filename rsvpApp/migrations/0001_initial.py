# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=200)),
                ('guest_attending', models.NullBooleanField()),
                ('guest_drink_pref', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RsvpResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('response_date', models.DateTimeField(verbose_name='responded on')),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp_response',
            field=models.ForeignKey(to='rsvpApp.RsvpResponse'),
        ),
    ]
