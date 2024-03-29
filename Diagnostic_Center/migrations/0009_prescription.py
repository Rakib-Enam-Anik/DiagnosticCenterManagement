# Generated by Django 5.0.2 on 2024-03-11 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0021_remove_doctorprofile_technician_doctorprofile_doctor_and_more'),
        ('Diagnostic_Center', '0008_packagetestappointment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=300, null=True)),
                ('text2', models.CharField(blank=True, max_length=300, null=True)),
                ('text3', models.CharField(blank=True, max_length=100, null=True)),
                ('date1', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.dcmpatient')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.test')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
