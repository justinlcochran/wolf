# Generated by Django 3.2.8 on 2021-11-01 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wolfapp', '0007_remove_role_role_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='role_type',
            field=models.ForeignKey(default='Baby', on_delete=django.db.models.deletion.CASCADE, related_name='type', to='wolfapp.roletype', to_field='role_type'),
        ),
    ]
