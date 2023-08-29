# Generated by Django 4.2.4 on 2023-08-28 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0031_remove_projectimage_project_project_primary_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectimage",
            name="Category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Home.category",
            ),
        ),
    ]