# -*- coding: utf-8 -*-
# Copyright 2017-2019 ControlScan, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distilleries', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('enabled', models.BooleanField(default=True)),
                ('time_interval', models.IntegerField()),
                ('time_unit', models.CharField(choices=[('s', 'Seconds'), ('m', 'Minutes'), ('h', 'Hours'), ('d', 'Days')], max_length=3)),
                ('alerts_enabled', models.BooleanField(default=True)),
                ('repeating_alerts', models.BooleanField(default=False)),
                ('alert_level', models.CharField(choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low'), ('INFO', 'Info')], max_length=20)),
                ('last_alert_date', models.DateTimeField(blank=True, null=True)),
                ('last_alert_id', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('RED', 'Red'), ('YELLOW', 'Yellow'), ('GREEN', 'Green')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('last_healthy', models.DateTimeField(blank=True, null=True)),
                ('last_saved_doc', models.CharField(blank=True, max_length=255, null=True, verbose_name='document id')),
                ('distilleries', models.ManyToManyField(related_name='_monitor_distilleries_+', to='distilleries.Distillery')),
                ('groups', models.ManyToManyField(blank=True, help_text='Only show Alerts to Users in these Groups. If no Groups are selected, Alerts will be visible to all Groups.', to='auth.Group')),
                ('last_active_distillery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distilleries.Distillery', verbose_name='distillery')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
