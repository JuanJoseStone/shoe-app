# Generated by Django 3.2.3 on 2021-07-03 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dozens', '0001_initial'),
        ('sizes', '0001_initial'),
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dozensofrematadores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rematadores', to=settings.AUTH_USER_MODEL, verbose_name='Rematadores'),
        ),
        migrations.AddField(
            model_name='dozensofcortadores',
            name='dozen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cortador', to='dozens.dozen', verbose_name='Docena'),
        ),
        migrations.AddField(
            model_name='dozensofcortadores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cortadores', to=settings.AUTH_USER_MODEL, verbose_name='Cortadores'),
        ),
        migrations.AddField(
            model_name='dozensofarmadores',
            name='dozen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='armador', to='dozens.dozen', verbose_name='Docena'),
        ),
        migrations.AddField(
            model_name='dozensofarmadores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='armadores', to=settings.AUTH_USER_MODEL, verbose_name='Armadores'),
        ),
        migrations.AddField(
            model_name='dozensofaparadores',
            name='dozen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='aparador', to='dozens.dozen', verbose_name='Docena'),
        ),
        migrations.AddField(
            model_name='dozensofaparadores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aparadores', to=settings.AUTH_USER_MODEL, verbose_name='Aparadores'),
        ),
        migrations.AddField(
            model_name='dozen',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dozens', to='model.model', verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='dozen',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dozens', to='sizes.sizes', verbose_name='Talla'),
        ),
    ]
