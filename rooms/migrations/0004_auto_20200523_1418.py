# Generated by Django 2.2.5 on 2020-05-23 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20200523_1415'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rule',
            new_name='HouseRule',
        ),
    ]
