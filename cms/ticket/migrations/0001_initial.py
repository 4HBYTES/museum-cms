# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ticket.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0002_auto_20170131_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=ticket.models.make_uuid, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('used', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.FrontUser')),
            ],
        ),
    ]