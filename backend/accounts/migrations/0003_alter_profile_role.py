# Generated by Django 5.1.6 on 2025-04-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('receptionist', 'Receptionist')], max_length=12),
        ),
    ]
