from django.urls import re_path
from Ventaxpersona import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    re_path(r'^persona/$',views.personaApi),
    re_path(r'^persona/([0-9]+)$',views.personaApi),

    re_path(r'^encabezado/$',views.EncabezadoApi),
    re_path(r'^encabezado/([0-9]+)$',views.EncabezadoApi),

    re_path(r'^encabezadodeta/$',views.EncabezadoDetaApi),
    re_path(r'^encabezadodeta/([0-9]+)$',views.EncabezadoDetaApi),
    
    re_path(r'^detalleov/$',views.ListaDetaxOrdenApi),
    re_path(r'^detalleov/([0-9]+)$',views.ListaDetaxOrdenApi),
]