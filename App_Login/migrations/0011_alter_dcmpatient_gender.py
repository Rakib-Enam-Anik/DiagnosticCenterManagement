# Generated by Django 5.0.2 on 2024-03-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0010_alter_technician_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcmpatient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, null=True),
        ),
    ]