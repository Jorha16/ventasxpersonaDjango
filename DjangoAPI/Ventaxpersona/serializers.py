from rest_framework import serializers
from Ventaxpersona.models import Persona, EncabezadoOrdenVenta, DetalleOrdenVenta


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Persona
        fields =('Cedula', 'Dereccion','Telefono', 'FechaNacimiento','Genero', 'Nombre','PrimerApellido', 'SegundoApellido','Correo')

class EncabezadoOVSerializer(serializers.ModelSerializer):
    class Meta:
        model =EncabezadoOrdenVenta
        fields =('IdOrdenVenta', 'IdPersona', 'IdSupermercado', 'MetodoPago', 'TipoCambio','FechaOrden')



class DetalleOVSerializer(serializers.ModelSerializer):
    class Meta:
        model =DetalleOrdenVenta
        fields =('IdLinea', 'IdOrdenVenta','IdProducto', 'NombreProdcuto','Unidad', 'PrecioUnit','PorcentajeImp', 'PrecioImpUnit','Cantidad','PrecioTotal')