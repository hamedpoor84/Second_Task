# Generated by Django 5.0.7 on 2025-02-20 10:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_followers_user_followings_user_profile_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_name",
        ),
    ]
