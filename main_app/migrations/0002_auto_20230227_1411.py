# Generated by Django 3.1.1 on 2023-02-27 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBulkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='students/bulkupload/')),
            ],
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='notificationstaff',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='session',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='session',
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='FeedbackStaff',
        ),
        migrations.DeleteModel(
            name='FeedbackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='NotificationStaff',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
        migrations.DeleteModel(
            name='StudentResult',
        ),
    ]
