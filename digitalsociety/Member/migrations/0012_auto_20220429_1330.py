# Generated by Django 3.0 on 2022-04-29 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0011_auto_20220429_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='EventView',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
