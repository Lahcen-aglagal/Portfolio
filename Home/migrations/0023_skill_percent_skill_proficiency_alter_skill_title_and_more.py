# Generated by Django 4.2.4 on 2023-08-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0022_remove_skill_percent_remove_skill_proficiency_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="percent",
            field=models.PositiveIntegerField(
                blank=True,
                default=0,
                help_text="Enter a value between 0 and 100",
                null=True,
                verbose_name="Proficiency Percentage",
            ),
        ),
        migrations.AddField(
            model_name="skill",
            name="proficiency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("beginner", "Beginner"),
                    ("intermediate", "Intermediate"),
                    ("advanced", "Advanced"),
                    ("expert", "Expert"),
                ],
                default="beginner",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="title",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Skill Title"
            ),
        ),
        migrations.DeleteModel(
            name="SkillTag",
        ),
    ]
