# Generated by Django 5.1.3 on 2024-12-17 14:15

import FiTrack.goal.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='target_date',
            field=models.DateField(validators=[FiTrack.goal.validators.validate_future_date]),
        ),
    ]
