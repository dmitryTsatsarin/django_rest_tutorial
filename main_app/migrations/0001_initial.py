# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('hobby', models.CharField(max_length=255, null=True, blank=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('album', models.ForeignKey(to='main_app.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='main_app.Artist'),
        ),
    ]
