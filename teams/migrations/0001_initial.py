# Generated by Django 4.0.10 on 2023-03-26 20:57

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        default=None, upload_to="media/team-images/"
                    ),
                ),
                ("code_name", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=256)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("domestic", "Domestic"),
                            ("international", "International"),
                            ("national", "National"),
                            ("league", "League"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=2, max_digits=2, null=True
                    ),
                ),
                ("champions", models.IntegerField(default=0)),
                (
                    "create_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 3, 26, 20, 57, 12, 403684, tzinfo=utc
                        )
                    ),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 3, 26, 20, 57, 12, 403708, tzinfo=utc
                        )
                    ),
                ),
            ],
        ),
    ]
