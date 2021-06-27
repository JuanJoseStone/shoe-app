# Generated by Django 3.2.3 on 2021-06-25 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sizes', '0002_auto_20210625_1728'),
        ('category', '0002_auto_20210625_1728'),
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='models', to='category.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=15, unique=True, verbose_name='Nombre del modelo'),
        ),
        migrations.AlterField(
            model_name='model',
            name='sizes',
            field=models.ManyToManyField(through='model.SizesAndModels', to='sizes.Sizes', verbose_name='Tallas'),
        ),
        migrations.AlterField(
            model_name='sizesandmodels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='sizesandmodels',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='model.model', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='sizesandmodels',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Précio'),
        ),
        migrations.AlterField(
            model_name='sizesandmodels',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sizes.sizes', verbose_name='Talla'),
        ),
        migrations.AlterField(
            model_name='sizesandmodels',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización'),
        ),
        migrations.AlterModelTable(
            name='sizesandmodels',
            table='models_sizes',
        ),
    ]
