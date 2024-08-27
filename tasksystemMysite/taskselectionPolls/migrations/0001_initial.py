# Generated by Django 4.2 on 2024-08-27 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("desc", models.TextField(max_length=200)),
                ("location", models.TextField(max_length=200)),
                ("code", models.IntegerField(unique=True)),
                ("date", models.DateField()),
                ("starttime", models.TimeField()),
                ("endtime", models.TimeField()),
                ("category", models.IntegerField(default=0)),
                (
                    "_is_sticky",
                    models.BooleanField(db_column="is_sticky", default=False),
                ),
                (
                    "sv",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
