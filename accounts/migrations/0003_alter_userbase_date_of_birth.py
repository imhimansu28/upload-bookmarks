# Generated by Django 4.0.10 on 2023-03-15 06:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0002_alter_userbase_options_alter_userbase_managers_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="userbase",
            name="date_of_birth",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]