# Generated by Django 5.1.2 on 2024-10-26 17:43

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), profiles.validators.AlphaNumeric()])),
                ('email', models.EmailField(max_length=254)),
                ('Age', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
