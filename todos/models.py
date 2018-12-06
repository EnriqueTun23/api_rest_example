from django.db import models

# Create your models here.

class Todos(models.Model):
    primer_nombre = models.CharField(max_length=256)
    segundo_nombre = models.CharField(max_length=256, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=256)
    apellido_materno = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    telefono = models.CharField(max_length=16, blank=True, null=True)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)
    fecha_de_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.primer_nombre, self.apellido_paterno)

    class Meta:
        managed = True
        db_table = 'Todo'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'