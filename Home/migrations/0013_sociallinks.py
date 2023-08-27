# Generated by Django 4.2.4 on 2023-08-26 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Home", "0012_remove_profile_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="sociallinks",
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
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="Facebook URL"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="Twitter URL"),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="LinkedIn URL"),
                ),
                (
                    "github",
                    models.URLField(blank=True, null=True, verbose_name="GitHub URL"),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True, null=True, verbose_name="Instagram URL"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
