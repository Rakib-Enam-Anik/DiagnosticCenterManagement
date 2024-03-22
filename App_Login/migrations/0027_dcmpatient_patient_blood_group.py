# Generated by Django 4.2.6 on 2024-03-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0026_dcmpatient_patient_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcmpatient',
            name='patient_blood_group',
            field=models.IntegerField(blank=True, choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, '0+'), (6, '0-'), (7, 'AB+'), (8, 'AB-')], null=True),
        ),
    ]