# Generated by Django 5.0.1 on 2024-02-26 11:02

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, validators=[core.validators.email_validator]),
        ),
    ]