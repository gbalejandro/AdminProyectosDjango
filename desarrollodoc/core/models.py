from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Proyecto')
    modulo = models.CharField(max_length=50, verbose_name='Módulo')
    descripcion = models.TextField(max_length=1500, verbose_name='Descripción')
    notas = models.TextField(max_length=1500, verbose_name='Notas')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    #creado_por = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario de creación')

    def __str__(self):
        return '{} {}'.format(self.nombre, self.modulo)


class Desarrollo(models.Model):
    version = models.CharField(max_length=50, verbose_name='Versión')
    consultas = models.TextField(max_length=1500, verbose_name='Consultas Relevantes')
    informacion = models.TextField(max_length=1500, verbose_name='Información del proyecto')
    proyecto = models.ForeignKey(Proyecto, null=True, on_delete=models.SET_NULL)

    DESA_STATUS = (
        ('t', 'Terminado'),
        ('d', 'En Desarrollo'),
        ('p', 'Pausado'),
        ('c', 'Cancelado'),
    )

    estatus = models.CharField(max_length=1, choices=DESA_STATUS, blank=True, default='d', help_text='Avance del Desarrollo')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return '{} {}'.format(self.id,self.proyecto.nombre)
