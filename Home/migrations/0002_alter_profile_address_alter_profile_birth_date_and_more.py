# Generated by Django 4.2.4 on 2023-08-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.CharField(max_length=100, null=True, verbose_name="Address"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(null=True, verbose_name="Birth date"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.CharField(max_length=100, null=True, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="degree",
            field=models.CharField(
                choices=[
                    ("bachelor", "Bachelor"),
                    ("master", "Master"),
                    ("phd", "PhD"),
                ],
                max_length=20,
                null=True,
                verbose_name="Degree",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(max_length=100, null=True, verbose_name="Phone"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="status",
            field=models.CharField(
                choices=[
                    ("married", "Married"),
                    ("single", "Single"),
                    ("divorced", "Divorced"),
                    ("widowed", "Widowed"),
                ],
                default="single",
                max_length=20,
                null=True,
                verbose_name="Status",
            ),
        ),
    ]
