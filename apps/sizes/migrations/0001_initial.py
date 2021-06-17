# Generated by Django 3.2.3 on 2021-06-17 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('note', models.TextField(blank=True, max_length=255, verbose_name='Nota')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
    ]
