# Generated by Django 5.0.2 on 2024-03-14 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0015_prescription_pres_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='pres_name',
        ),
    ]