# Generated by Django 4.2.4 on 2023-08-26 22:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Home", "0014_alter_skill_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Skill",
            new_name="Skills",
        ),
    ]
