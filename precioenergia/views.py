'''
Created on Apr 8, 2014

@author: gonzmg
'''
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

from google.appengine.api import users

from precioenergia.models import PrecioEnergia

import urllib
from urllib2 import urlopen
import datetime
from pytz import timezone
import pytz
from operator import itemgetter, attrgetter
import json

from django.http import HttpResponse

import logging
from django.template.defaultfilters import length
from django.core.serializers.json import DjangoJSONEncoder


def main_page(request):
    tz_madrid = timezone('Europe/Madrid')
    fecha_query = datetime.datetime.now(pytz.utc).astimezone(tz_madrid).replace(hour=0, minute=0, second=0, microsecond=0)
        
    template_values = {
       'date' : fecha_query.strftime("%Y-%m-%d %H:%M")
    }
    return direct_to_template(request, 'precioenergia/main_page.html', template_values)

def EnviarDatos(request):
    tz_madrid = timezone('Europe/Madrid')
    fecha_query = datetime.datetime.now(pytz.utc).astimezone(tz_madrid).replace(hour=0, minute=0, second=0, microsecond=0)
    fecha_inicial = fecha_query - datetime.timedelta(days=7)
    fecha_final = fecha_query + datetime.timedelta(days=1)
    
    # Recupero los datos de la bbdd
    query_contenido = PrecioEnergia.query(PrecioEnergia.fecha >= fecha_inicial)
    contenido = query_contenido.fetch()
    
    if (len(contenido) == 0):
        logging.info("bbdd Vacia")
    else:
        logging.info("bbdd con datos")
    # Calculo los dias missing y vuelvo a buscarlos
    while (fecha_inicial <= fecha_final):
        fecha_inicial_utc = fecha_inicial.astimezone(pytz.utc)
        rango = filter(lambda x: pytz.utc.localize(x.fecha_prediccion) == fecha_inicial_utc, contenido)
        if (len(rango) == 0):
            contenido.extend(ProcesarDatos(fecha_inicial))
            contenido = sorted(contenido, key=attrgetter('fecha'))
        
        fecha_inicial += datetime.timedelta(days=1)
    
    content = map(lambda linea : [ pytz.utc.localize(linea.fecha).astimezone(tz_madrid),linea.precio_espana,linea.precio_portugal],contenido)
#     for linea in contenido:
#         content.append("[new Date(\"" + pytz.utc.localize(linea.fecha).astimezone(tz_madrid).strftime("%Y-%m-%d %H:%M") + "\")" + "," + str(linea.precio_espana) + "," + str(linea.precio_portugal) + "]")
#    str_contenido = "[" + ",\n".join(content) + "]"

    json_obj = json.dumps(content,cls=DjangoJSONEncoder)

    return HttpResponse(json_obj,mimetype='application/json')

    

def ProcesarDatos(fecha):
    contenido = []
    tz_madrid = timezone('Europe/Madrid')
    logging.info("Solicitando datos para fecha: " + fecha.strftime("%Y-%m-%d %H:%M"))
    try:
        datos = urlopen("http://www.omie.es/datosPub/marginalpdbc/marginalpdbc_" + fecha.strftime("%Y%m%d") + ".1")
        datos.readline()  # Quitamos la primera linea
        for linea in datos:
            fila = linea.strip(';\r\n').split(';')
            if (len(fila) >= 6):
                dato = PrecioEnergia()
                dato.fecha = datetime.datetime(year=int(fila[0]), month=int(fila[1]), day=int(fila[2]), hour=int(fila[3]) - 1, minute=0, tzinfo=tz_madrid).astimezone(pytz.utc).replace(tzinfo=None)
                dato.fecha_prediccion = fecha.astimezone(pytz.utc).replace(tzinfo=None)
                dato.precio_espana = float(fila[4]) 
                dato.precio_portugal = float(fila[5]) 
                dato.put()
                contenido.append(dato)
            
    except IOError:
        logging.warning("No se ha podido recuperar el archivo de la fecha: " + fecha.strftime("%Y-%m-%d"))
        
    return contenido

