# Generated by Django 5.0.2 on 2024-03-14 07:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0021_remove_doctorprofile_technician_doctorprofile_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='attendent_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_attendent',
            field=models.BooleanField(default=False),
        ),
    ]
