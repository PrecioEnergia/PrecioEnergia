'''
Created on Apr 8, 2014

@author: gonzmg
'''
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

from google.appengine.api import users

from precioenergia.models import Greeting

import urllib
from urllib2 import urlopen
import datetime
from datetime import tzinfo
#import pytz

def main_page(request):
    datos = urlopen("http://www.omie.es/datosPub/marginalpdbc/marginalpdbc_"+datetime.datetime.utcnow().strftime("%Y%m%d")+".1")
    
    # Esto deberia ser una funcion
    contenido = []
    datos.readline() # Quitamos la primera linea
    for linea in datos:
        contenido.append(linea.strip(';\r\n').split(';'))
    
    content=[]
    for linea in contenido:
        if (len(linea)>=6):
            content.append("[new Date(\""+"-".join(linea[0:3])+" "+str(int(linea[3])-1)+":00\")"+","+linea[5]+"]")
    
    str_contenido ="["+ ",\n".join(content)+"]"
    
    template_values = {
        'str_contenido' : str_contenido,
    }
    return direct_to_template(request, 'precioenergia/main_page.html', template_values)