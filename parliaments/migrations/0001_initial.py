# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json
import parliaments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parliament',
            fields=[
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('number', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('seats', models.PositiveSmallIntegerField(help_text='Aggregate', null=True)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Parliamentarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('names', django_extensions.db.fields.json.JSONField(default=dict)),
                ('photo', models.ImageField(upload_to=parliaments.models.get_photo_path)),
                ('birthtext', models.CharField(db_index=True, help_text='Exact birth dates for parliamentarians in the 1800s sometimes omitted day or month', max_length=10)),
                ('birthdate', models.DateField(db_index=True, null=True)),
                ('lop_item_code', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('names', django_extensions.db.fields.json.JSONField(default=dict)),
                ('color', models.CharField(max_length=20)),
                ('lop_item_code', models.SlugField(null=True)),
                ('related', models.ManyToManyField(blank=True, related_name='_party_related_+', to='parliaments.Party')),
            ],
            options={
                'verbose_name_plural': 'parties',
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('names', django_extensions.db.fields.json.JSONField(default=dict)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Riding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('names', django_extensions.db.fields.json.JSONField(default=dict)),
                ('electoral_district_number', models.PositiveIntegerField(db_index=True, null=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ridings', to='parliaments.Province')),
                ('related_geographically', models.ManyToManyField(blank=True, related_name='_riding_related_geographically_+', to='parliaments.Riding')),
                ('related_historically', models.ManyToManyField(blank=True, related_name='_riding_related_historically_+', to='parliaments.Riding')),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', django_extensions.db.fields.json.JSONField(default=dict)),
                ('number', models.PositiveSmallIntegerField(db_index=True)),
                ('date_start', models.DateField(db_index=True)),
                ('date_end', models.DateField(db_index=True, null=True)),
                ('sittings_house', models.PositiveSmallIntegerField()),
                ('sittings_senate', models.PositiveSmallIntegerField()),
                ('parliament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='parliaments.Parliament')),
            ],
            options={
                'ordering': ('parliament__number', 'number'),
            },
        ),
        migrations.AddField(
            model_name='parliament',
            name='government_party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='governed_parliaments', to='parliaments.Party'),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('parliament', 'number')]),
        ),
    ]