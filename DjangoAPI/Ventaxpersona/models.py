from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Persona(models.Model):
    Cedula = models.CharField(primary_key=True, unique=True, max_length=15)
    Dereccion = models.CharField(max_length=300)
    Telefono = models.CharField(max_length=10)
    FechaNacimiento =  models.DateField()
    Genero = models.BooleanField()
    Nombre = models.CharField(max_length=30)
    PrimerApellido = models.CharField(max_length=30)
    SegundoApellido = models.CharField(max_length=30)
    Correo = models.CharField(max_length=100)


class EncabezadoOrdenVenta(models.Model):
    Metodos_de_pago = [
    ('Dolares', 'Dolares'),
    ('Colones', 'Colones'),
    ]
    IdOrdenVenta = models.AutoField(primary_key=True)
    IdPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    IdSupermercado = models.CharField(max_length=15)
    MetodoPago = models.CharField(max_length=30,choices=Metodos_de_pago,default='Colones')
    TipoCambio = models.IntegerField(default=1)
    FechaOrden =  models.DateField()

class DetalleOrdenVenta(models.Model):
    IdLinea = models.AutoField(primary_key=True)
    IdOrdenVenta =  models.ForeignKey(EncabezadoOrdenVenta, on_delete=models.CASCADE)
    IdProducto = models.IntegerField()
    NombreProdcuto = models.CharField(max_length=50)
    Unidad = models.CharField(max_length=50)
    PrecioUnit = models.DecimalField(max_digits=8, decimal_places=2)
    PorcentajeImp =models.DecimalField(max_digits=8, decimal_places=2)
    PrecioImpUnit = models.DecimalField( max_digits=8, decimal_places=2)
    Cantidad = models.IntegerField()
    PrecioTotal = models.DecimalField( max_digits=8, decimal_places=2)
