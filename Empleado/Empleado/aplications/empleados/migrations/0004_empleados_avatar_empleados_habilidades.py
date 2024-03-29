# Generated by Django 4.1.4 on 2023-01-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empleados", "0003_habilidades_rename_empleado_empleados_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="empleados",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="empleado"),
        ),
        migrations.AddField(
            model_name="empleados",
            name="habilidades",
            field=models.ManyToManyField(to="empleados.habilidades"),
        ),
    ]
