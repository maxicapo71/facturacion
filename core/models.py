from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    provincia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Planes(models.Model):
    nombre = models.CharField(max_length=50)
    vel_subida = models.IntegerField(verbose_name="Velocidad de Subida Kb")
    vel_bajada = models.IntegerField(verbose_name="Velocidad de Descarga Kb")
    precio = models.IntegerField()
    detalle = models.TextField(max_length=160)

    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plan = models.ForeignKey(Planes, on_delete=models.PROTECT)
    ip = models.GenericIPAddressField(verbose_name="Direccion IP")
    detalle = models.TextField(max_length=160)
    fecha_creacion = models.DateField(default=timezone.now)


    def __str__(self):
        return self.ip



