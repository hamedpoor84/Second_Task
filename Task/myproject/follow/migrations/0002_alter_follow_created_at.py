# Generated by Django 5.0.7 on 2025-02-19 19:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("follow", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
