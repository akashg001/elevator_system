# Generated by Django 4.2.2 on 2023-06-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Elevator",
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
                ("name", models.CharField(max_length=100)),
                ("current_floor", models.IntegerField(default=0)),
                ("is_moving", models.BooleanField(default=False)),
                (
                    "direction",
                    models.CharField(
                        choices=[("up", "Up"), ("down", "Down"), ("stop", "Stop")],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
