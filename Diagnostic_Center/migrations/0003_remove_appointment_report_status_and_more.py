# Generated by Django 5.0.2 on 2024-02-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0002_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='report_status',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]