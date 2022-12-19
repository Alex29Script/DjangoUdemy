# Generated by Django 4.1.4 on 2022-12-19 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin_Modelo",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "shor_name",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Nombre Corto"
                    ),
                ),
                ("anulate", models.BooleanField(default=False, verbose_name="Anulado")),
            ],
        ),
    ]
