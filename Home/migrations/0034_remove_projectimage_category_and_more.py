# Generated by Django 4.2.4 on 2023-08-28 17:11

import Home.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0033_projectimage_project_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectimage",
            name="Category",
        ),
        migrations.RemoveField(
            model_name="projectimage",
            name="project_name",
        ),
        migrations.AddField(
            model_name="projectimage",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="Home.project",
            ),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="image",
            field=models.ImageField(
                null=True, upload_to=Home.models.image_upload_path, verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="title",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Image Title"
            ),
        ),
    ]
