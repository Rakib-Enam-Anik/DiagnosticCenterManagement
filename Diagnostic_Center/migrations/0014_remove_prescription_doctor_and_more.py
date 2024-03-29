# Generated by Django 5.0.2 on 2024-03-14 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0013_remove_prescription_test_prescription_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='test',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='user',
        ),
        migrations.AddField(
            model_name='prescription',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.doctorappointment'),
        ),
    ]
