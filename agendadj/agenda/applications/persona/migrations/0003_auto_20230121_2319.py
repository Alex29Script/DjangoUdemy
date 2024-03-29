# Generated by Django 3.0.5 on 2023-01-21 23:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20230121_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'Hobby', 'verbose_name_plural': 'Hobbies'},
        ),
        migrations.AddField(
            model_name='reunion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reunion',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reunion',
            name='persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='persona.Person'),
            preserve_default=False,
        ),
    ]
