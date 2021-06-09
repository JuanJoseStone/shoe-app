# Generated by Django 3.2.3 on 2021-06-07 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('types', models.CharField(max_length=250, verbose_name='Tipos')),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Cantidad')),
                ('colors', models.CharField(max_length=250, null=True, verbose_name='Colores')),
                ('type', models.CharField(max_length=250, verbose_name='Tipo de material')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Tipo de material')),
                ('note', models.TextField(max_length=255, null=True, verbose_name='Nota')),
                ('created_at', models.DateField(auto_now=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventory', to='apps.material', verbose_name='Inventario')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
    ]
