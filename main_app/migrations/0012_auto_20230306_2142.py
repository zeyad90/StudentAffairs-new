# Generated by Django 3.1.1 on 2023-03-06 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20230306_2136'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Semseter',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Semseter',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Semseter',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='Semseter',
            new_name='course',
        ),
    ]
