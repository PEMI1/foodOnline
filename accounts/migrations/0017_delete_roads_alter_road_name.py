# Generated by Django 4.1.4 on 2023-03-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_road_delete_roads'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='road',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
