# Generated by Django 5.0.2 on 2024-02-28 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0005_rename_patient_dcmadmin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_first_name',
            field=models.CharField(blank=True, default='Dr.', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dcmadmin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
