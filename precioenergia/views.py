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
import logging

def main_page(request):
    tz_madrid = timezone('Europe/Madrid')
    fecha_query = datetime.datetime.now(pytz.utc).astimezone(tz_madrid)
    fecha_inicial = fecha_query - datetime.timedelta(days=7)
    fecha_final = fecha_query + datetime.timedelta(days=1)
    
    contenido = []
    while (fecha_inicial <= fecha_final):
        try:
            datos = urlopen("http://www.omie.es/datosPub/marginalpdbc/marginalpdbc_" + fecha_inicial.strftime("%Y%m%d") + ".1")
            datos.readline()  # Quitamos la primera linea
            for linea in datos:
                fila = linea.strip(';\r\n').split(';')
                if (len(fila)>=6):
                    contenido.append([datetime.datetime(year=int(fila[0]), month=int(fila[1]), day=int(fila[2]), hour=int(fila[3]) - 1,minute=0), fila[4], fila[5]])
                
        except IOError:
            logging.warning("No se ha podido recuperar el archivo de la fecha: " + fecha_inicial.strftime("%Y-%m-%d"))
        fecha_inicial += datetime.timedelta(days=1)
    # Esto deberia ser una funcion
    
    content = []
    for linea in contenido:
        content.append("[new Date(\"" + linea[0].strftime("%Y-%m-%d %H:%M") + "\")" + "," + linea[1] + "," + linea[2] + "]")
    
    str_contenido = "[" + ",\n".join(content) + "]"
    
    template_values = {
        'str_contenido' : str_contenido,
        'date' : fecha_query.strftime("%Y-%m-%d %H:%M")
    }
    return direct_to_template(request, 'precioenergia/main_page.html', template_values)
