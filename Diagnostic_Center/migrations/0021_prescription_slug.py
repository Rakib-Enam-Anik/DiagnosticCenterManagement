# Generated by Django 4.2.6 on 2024-03-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0020_prescription_pres_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='slug',
            field=models.SlugField(blank=True, max_length=264, null=True, unique=True),
        ),
    ]