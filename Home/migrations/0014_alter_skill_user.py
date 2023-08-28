# Generated by Django 4.2.4 on 2023-08-26 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Home", "0013_sociallinks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="user",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]