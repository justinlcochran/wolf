# Generated by Django 3.2.8 on 2021-11-01 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wolfapp', '0006_auto_20211031_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='role_type',
        ),
    ]