# Generated by Django 5.0.2 on 2024-03-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0011_alter_dcmpatient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcmpatient',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]