# Generated by Django 3.0 on 2022-04-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chairman', '0004_auto_20220421_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='no_of_vehicles',
            field=models.CharField(default='', max_length=100),
        ),
    ]
