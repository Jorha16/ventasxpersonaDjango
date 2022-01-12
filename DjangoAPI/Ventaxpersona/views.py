from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from django.core.files.storage import default_storage

from Ventaxpersona.models import Persona, EncabezadoOrdenVenta,DetalleOrdenVenta
from Ventaxpersona.serializers import PersonaSerializer, EncabezadoOVSerializer, DetalleOVSerializer

# Create your views here.
 # Create your views Employees.
@csrf_exempt
def personaApi(request, id=0):
    if request.method == 'GET':
        persona = Persona.objects.all()
        persona_serializer = PersonaSerializer(persona, many=True)
        return JsonResponse(persona_serializer.data, safe=False)

    
@csrf_exempt
def EncabezadoApi(request, id=0):
    if request.method == 'GET':
        encabezado = EncabezadoOrdenVenta.objects.all()
        encabezado_serializer = EncabezadoOVSerializer(encabezado, many=True)
        return JsonResponse(encabezado_serializer.data, safe=False)

    elif request.method == 'POST':
        encabezadoOV_data = JSONParser().parse(request)
        encabezadoOV_serializer = EncabezadoOVSerializer(data=encabezadoOV_data)
        if encabezadoOV_serializer.is_valid():
            encabezadoOV_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)

@csrf_exempt
def EncabezadoDetaApi(request, id=0): 
    if request.method == 'GET':
        if ('IdPersona' in request.GET):
            encabezado = EncabezadoOrdenVenta.objects.filter(IdPersona=request.GET['IdPersona'])
           # orden = DetalleOrdenVenta.objects.filter(EncabezadoOrdenVenta.IdOrdenVenta= encabezado.IdOrdenVenta)
            encabezado_serializer = EncabezadoOVSerializer(encabezado, many=True)
        else:
             encabezado = EncabezadoOrdenVenta.objects.all()
             encabezado_serializer = EncabezadoOVSerializer(encabezado, many=True)
        return JsonResponse(encabezado_serializer.data, safe=False)

@csrf_exempt
def ListaDetaxOrdenApi(request, id=0): 
    if request.method == 'GET':
        if ('IdOrdenVenta' in request.GET):
            detalleov = DetalleOrdenVenta.objects.filter(IdOrdenVenta=request.GET['IdOrdenVenta'])
            detalleov_serializer = DetalleOVSerializer(detalleov, many=True)
        else:
             detalleov = DetalleOrdenVenta.objects.all()
             detalleov_serializer = DetalleOVSerializer(detalleov, many=True)
        return JsonResponse(detalleov_serializer.data, safe=False)

@csrf_exempt
def DetalleOVApi(request, id=0):
    if request.method == 'GET':
        detalleov = DetalleOrdenVenta.objects.all()
        detalleov_serializer = DetalleOVSerializer(detalleov, many=True)
        return JsonResponse(detalleov_serializer.data, safe=False)

    elif request.method == 'POST':
        detalleOV_data = JSONParser().parse(request)
        detalleOV_serializer = DetalleOVSerializer(data=detalleOV_data)
        if detalleOV_serializer.is_valid():
            detalleOV_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)