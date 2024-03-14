# Generated by Django 5.0.2 on 2024-03-14 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0023_dcmpatient_attendent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='App_Login.attendent')),
            ],
        ),
    ]