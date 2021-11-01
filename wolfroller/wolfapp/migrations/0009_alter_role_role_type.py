# Generated by Django 3.2.8 on 2021-11-01 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wolfapp', '0008_role_role_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.ForeignKey(default='Villager', on_delete=django.db.models.deletion.CASCADE, related_name='type', to='wolfapp.roletype', to_field='role_type'),
        ),
    ]