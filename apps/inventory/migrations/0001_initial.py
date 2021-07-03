# Generated by Django 3.2.3 on 2021-07-03 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers_and_customers', '0001_initial'),
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Cantidad')),
                ('stock', models.IntegerField(verbose_name='Existencias')),
                ('color', models.CharField(blank=True, choices=[('negro', 'negro'), ('plomo', 'plomo'), ('cafe', 'cafe'), ('amarillo', 'amarillo'), ('verde', 'verde'), ('blanco', 'rojo'), ('azul', 'azul'), ('rojo', 'rojo')], max_length=15, verbose_name='Color')),
                ('type', models.CharField(blank=True, max_length=250, verbose_name='Tipo de material')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio')),
                ('note', models.TextField(blank=True, max_length=255, verbose_name='Nota')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inventory', to='materials.material', verbose_name='Material')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inventory', to='providers_and_customers.providersandcustomers', verbose_name='Proveedor')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
    ]
