# Generated by Django 3.1.1 on 2023-03-06 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20230306_2142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Semester',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='course',
            new_name='Semester',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='Semester',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='course',
            new_name='Semester',
        ),
    ]