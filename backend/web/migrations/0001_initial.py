# Generated by Django 4.1.3 on 2023-06-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("article_id", models.UUIDField()),
                ("title", models.TextField()),
                ("author", models.TextField()),
                ("date_published", models.DateTimeField()),
                ("textual_content", models.TextField()),
            ],
        ),
    ]
