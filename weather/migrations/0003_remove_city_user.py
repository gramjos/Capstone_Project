# Generated by Django 4.1.1 on 2022-10-09 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
    ]
