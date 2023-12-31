# Generated by Django 4.2.4 on 2023-08-28 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0035_alter_projectimage_project"),
    ]

    operations = [
        migrations.AlterField(
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
            name="title",
            field=models.CharField(
                choices=[("primary", "Primary"), ("secondary", "Secondary")],
                max_length=100,
                null=True,
                verbose_name="Image Title",
            ),
        ),
    ]
