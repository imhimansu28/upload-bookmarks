# Generated by Django 4.0.10 on 2023-03-21 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookmark", "0003_uploadbookmark"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UploadBookmark",
        ),
    ]