# Generated by Django 3.1.1 on 2023-03-05 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_customuser_innumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='innumber',
            new_name='idnumber',
        ),
    ]
