from django.db import models

# Create your models here.
class ProvidersAndCustomers(models.Model):

    statuses = (
        ('inactivo', 'inactivo'),
        ('activo', 'activo'),
    )
    
    types = (
        ('cliente', 'cliente'),
        ('proveedor', 'proveedor'),
    )

    types = models.CharField(max_length=10, choices=types, default='cliente', verbose_name='¿Proveedor o Cliente?')
    names_full = models.CharField(max_length=50, verbose_name='Nombres y apellidos')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Teléfono')
    email = models.CharField(max_length=30, blank=True, verbose_name='Email')
    status = models.CharField(max_length=10, choices=statuses, default='activo', verbose_name='Estado')
    direction = models.TextField(max_length=255, blank=True, verbose_name='Direción')
    description = models.TextField(max_length=255, blank=True, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'providers_and_custormers'

    def __str__(self):
        return self.names_full