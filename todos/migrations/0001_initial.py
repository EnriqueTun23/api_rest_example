# Generated by Django 2.1.1 on 2018-12-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=256)),
                ('segundo_nombre', models.CharField(blank=True, max_length=256, null=True)),
                ('apellido_paterno', models.CharField(max_length=256)),
                ('apellido_materno', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('telefono', models.CharField(blank=True, max_length=16, null=True)),
                ('fecha_de_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'db_table': 'Todo',
                'managed': True,
            },
        ),
    ]
