# Generated by Django 4.1.4 on 2023-01-31 16:38

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_roads_delete_localaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(max_length=12)),
                ('code', models.IntegerField()),
                ('fclass', models.CharField(max_length=28)),
                ('name', models.CharField(max_length=100, null=True)),
                ('ref', models.CharField(max_length=20, null=True)),
                ('oneway', models.CharField(max_length=1)),
                ('maxspeed', models.IntegerField(null=True)),
                ('layer', models.BigIntegerField()),
                ('bridge', models.CharField(max_length=1)),
                ('tunnel', models.CharField(max_length=1)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
       
    ]