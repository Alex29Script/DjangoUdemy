# Generated by Django 3.0.5 on 2023-01-21 22:58

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hobby', models.CharField(max_length=50, verbose_name='Pasa Tiempo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('asunto', models.CharField(max_length=100, verbose_name='asunto de la reunion')),
            ],
            options={
                'verbose_name': 'Reunion',
                'verbose_name_plural': 'Reuniones',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.AddField(
            model_name='person',
            name='hobby',
            field=models.ManyToManyField(to='persona.Hobby'),
        ),
    ]
