# Generated by Django 3.1.1 on 2023-02-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20230227_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
