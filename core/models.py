from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MaxLengthValidator



# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    dni = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField(validators=[MaxValueValidator(9999),MinValueValidator(1000)])
    provincia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Planes(models.Model):
    nombre = models.CharField(max_length=50)
    vel_subida = models.IntegerField(verbose_name="Velocidad de Subida Kb")
    vel_bajada = models.IntegerField(verbose_name="Velocidad de Descarga Kb")
    precio = models.IntegerField(validators=[MinValueValidator(1)])
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
        return self.cliente.nombre + "[" + self.ip + "]"


class Cupon(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    monto = models.IntegerField()
    detalle = models.TextField(max_length=160, null=True, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)
    pagado = models.BooleanField(False)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.cliente.nombre

class Usuarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
