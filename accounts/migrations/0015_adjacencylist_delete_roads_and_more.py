# Generated by Django 4.1.4 on 2023-02-05 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_datastatus_delete_roads'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjacencyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
     
        migrations.AddField(
            model_name='datastatus',
            name='adjacency_list_created',
            field=models.BooleanField(default=False),
        ),
    ]
