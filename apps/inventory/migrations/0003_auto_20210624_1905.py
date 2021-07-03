# Generated by Django 3.2.3 on 2021-06-25 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers_and_customers', '0001_initial'),
        ('inventory', '0002_auto_20210624_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='provider',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='inventories', to='providers_and_customers.providersandcustomers', verbose_name='Proveedor'),
        ),
    ]